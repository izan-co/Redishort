"""
Video Assembler Module
----------------------
Combines assets (video, audio, script) into final vertical video.
This is the creative heart of the project.
"""

import random
import logging
import shutil
import threading
from pathlib import Path
from contextlib import contextmanager
from functools import lru_cache
import numpy as np
from scipy.special import expit
from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip
from moviepy.video.VideoClip import VideoClip
from moviepy.config import change_settings
from moviepy.video.fx.all import crop, resize
from tqdm import tqdm
from config import (
    SEGMENTS_FOLDER, WHISPER_MODEL, IMAGEMAGICK_PATH,
    VIDEO_RESOLUTION, VIDEO_FPS, VIDEO_BITRATE, AUDIO_BITRATE, VIDEO_PRESET, ASPECT_RATIO,
    SUBTITLE_FONT, SUBTITLE_FONTSIZE, SUBTITLE_COLOR, SUBTITLE_STROKE_COLORS, SUBTITLE_STROKE_WIDTH,
    MIN_SEGMENT_SIZE_BYTES
)

logger = logging.getLogger(__name__)


@lru_cache(maxsize=1)
def setup_imagemagick():
    """Verify ImageMagick exists and configure moviepy to use it."""
    if not shutil.which(IMAGEMAGICK_PATH):
        raise FileNotFoundError("ImageMagick required but not found.")
    change_settings({"IMAGEMAGICK_BINARY": IMAGEMAGICK_PATH})


# Run on module import
setup_imagemagick()


class SegmentManager:
    """
    Manages assignment and consumption of background video segments.
    Ensures a segment is assigned to a single story and deleted after use.
    """

    def __init__(self):
        self._assigned = {}
        self._lock = threading.Lock()

    def get_segment(self, story_id: str) -> str:
        """Assign a random valid segment to a story ID."""
        with self._lock:
            if story_id in self._assigned:
                return self._assigned[story_id]
            segment = self._select_valid_segment()
            self._assigned[story_id] = segment
            logger.info(f"Segment '{Path(segment).name}' assigned to story '{story_id}'.")
            return segment

    def _select_valid_segment(self) -> str:
        """Select a random video segment from the segments folder."""
        segments_path = Path(SEGMENTS_FOLDER)
        available = [p for p in segments_path.glob("*.mp4") if p.stat().st_size >= MIN_SEGMENT_SIZE_BYTES]
        if not available:
            raise ValueError("No valid segments available.")
        return str(random.choice(available))

    def consume_segment(self, story_id: str):
        """Delete the segment associated with a story after upload."""
        with self._lock:
            if story_id in self._assigned:
                path = Path(self._assigned.pop(story_id))
                if path.exists():
                    path.unlink()
                    logger.info(f"Segment consumed and deleted: {path.name}")


# Global segment manager instance
segment_manager = SegmentManager()


def sigmoid_ease(t: float, duration: float, steepness: int = 10) -> float:
    """Sigmoid easing function for smooth progress bar animation."""
    return expit(steepness * (t / duration - 0.5))


def create_neon_progress_bar(duration: float, size: tuple) -> VideoClip:
    """Create an animated progress bar with color gradient and smooth easing."""
    width, height = size
    bar_height = max(10, int(height / 100))
    colors = np.array([np.linspace([255, 69, 0], [73, 182, 194], width)]).T.astype(np.uint8)

    def make_frame_rgb(t):
        progress = sigmoid_ease(t, duration)
        current_length = int(progress * width)
        frame = np.zeros((height, width, 3), dtype=np.uint8)
        if current_length > 0:
            frame[height-bar_height:height, :current_length] = colors[:current_length][np.newaxis, :, :]
        return frame

    def make_frame_mask(t):
        progress = sigmoid_ease(t, duration)
        mask = np.zeros((height, width), dtype=np.float32)
        if int(progress * width) > 0:
            mask[height-bar_height:height, :int(progress * width)] = 1.0
        return mask

    return VideoClip(make_frame_rgb, duration=duration).set_mask(
        VideoClip(make_frame_mask, duration=duration, ismask=True)
    )


@contextmanager
def managed_clip(clip_path: str, clip_type: str = 'video'):
    """Context manager to safely open and close moviepy clips, preventing memory leaks."""
    clip = VideoFileClip(clip_path) if clip_type == 'video' else AudioFileClip(clip_path)
    try:
        yield clip
    finally:
        clip.close()


def transcribe_audio(audio_path: str, whisper_model) -> list:
    """Transcribe audio file to get word-level timestamps."""
    result = whisper_model.transcribe(audio_path, word_timestamps=True, fp16=False)
    return [w for s in result.get('segments', []) for w in s.get('words', [])]


def create_subtitle_clip(text: str, video_size: tuple, y_pos: int, border_color: str) -> CompositeVideoClip:
    """Create a subtitle clip with solid border and high contrast."""
    width = int(video_size[0] * 0.9)

    # Border layer
    border = TextClip(
        text, fontsize=SUBTITLE_FONTSIZE, font=SUBTITLE_FONT,
        color=border_color, stroke_color=border_color, stroke_width=SUBTITLE_STROKE_WIDTH,
        method='caption', align='center', size=(width, None)
    )

    # Text layer
    main_text = TextClip(
        text, fontsize=SUBTITLE_FONTSIZE, font=SUBTITLE_FONT,
        color=SUBTITLE_COLOR, method='caption', align='center', size=(width, None)
    ).set_position("center")

    return CompositeVideoClip([border, main_text]).set_position(('center', y_pos))


def generate_subtitles(audio_path: str, video_size: tuple, whisper_model, narrator_gender: str) -> list:
    """
    Generate list of subtitle clips (TextClip), one per word,
    with correct start time and duration.
    """
    y_pos = int(video_size[1] * 0.4)
    color = SUBTITLE_STROKE_COLORS.get(narrator_gender, SUBTITLE_STROKE_COLORS["neutral"])

    result = whisper_model.transcribe(audio_path, word_timestamps=True, fp16=False)
    words = [w for s in result.get('segments', []) for w in s.get('words', [])]

    clips = []
    for w in tqdm(words, desc="Generating subtitles"):
        text = w.get('word', '').strip().upper()
        if not text:
            continue
        start = w['start']
        duration = max(w['end'] - w['start'], 0.1)
        clip = create_subtitle_clip(text, video_size, y_pos, color).set_start(start).set_duration(duration)
        clips.append(clip)

    return clips


def crop_to_aspect_ratio(video_clip, target_ratio: float):
    """Crop video to fit the target aspect ratio (9:16)."""
    w, h = video_clip.size
    current_ratio = w / h
    if current_ratio > target_ratio:
        new_width = int(h * target_ratio)
        return crop(video_clip, width=new_width, x_center=w/2)
    else:
        new_height = int(w / target_ratio)
        return crop(video_clip, height=new_height, y_center=h/2)


def assemble_viral_video(background_video_path: str, audio_path: str, output_filename: str,
                         whisper_model, narrator_gender: str):
    """
    Main function that orchestrates complete video assembly.
    Combines background video, audio, subtitles, and progress bar.
    """
    logger.info(f"Assembling final video: {Path(output_filename).name}")

    try:
        with managed_clip(audio_path, 'audio') as audio_clip:
            with managed_clip(background_video_path, 'video') as video_clip:
                duration = audio_clip.duration

                # Trim or loop video to match audio duration
                if video_clip.duration > duration:
                    video = video_clip.subclip(0, duration)
                else:
                    video = video_clip.set_duration(duration)

                # Crop and resize to vertical format
                video = crop_to_aspect_ratio(video, ASPECT_RATIO)
                video = resize(video, height=VIDEO_RESOLUTION[1], width=VIDEO_RESOLUTION[0])

                # Generate subtitles
                subtitle_clips = generate_subtitles(audio_path, video.size, whisper_model, narrator_gender)

                # Create progress bar
                progress_bar = create_neon_progress_bar(duration, video.size)

                # Compose final video
                final = CompositeVideoClip(
                    [video] + subtitle_clips + [progress_bar]
                ).set_audio(audio_clip).set_duration(duration)

                # Export
                final.write_videofile(
                    output_filename,
                    codec="libx264",
                    audio_codec="aac",
                    fps=VIDEO_FPS,
                    preset=VIDEO_PRESET,
                    threads=8,
                    logger='bar',
                    bitrate=VIDEO_BITRATE
                )

        logger.info(f"✅ Video assembled successfully: {Path(output_filename).name}")

    except Exception as e:
        logger.error(f"Error assembling video: {e}", exc_info=True)


def get_random_video_segment(story_id: str) -> str:
    """Convenience function to get a segment from the manager."""
    return segment_manager.get_segment(story_id)
