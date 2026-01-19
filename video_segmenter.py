"""
Video Segmenter Module
----------------------
Processes raw long-form videos into short segments.
Includes quality validation to ensure usable output.
"""

import subprocess
import re
import logging
import math
import cv2
import numpy as np
from pathlib import Path
from config import (
    RAW_VIDEOS_FOLDER, SEGMENTS_FOLDER, PROCESSED_VIDEOS_LOG, FFMPEG_PATH,
    SEGMENT_DURATION_SECONDS, ENABLE_VIDEO_TRIMMING, TRIM_START_SECONDS, TRIM_END_SECONDS,
    ENABLE_QUALITY_VALIDATION, VALIDATION_FRAME_SAMPLES,
    MIN_BRIGHTNESS, MAX_BRIGHTNESS, MIN_MOTION_SCORE
)

logger = logging.getLogger(__name__)


def is_segment_high_quality(segment_path: Path) -> tuple[bool, str]:
    """
    Validate segment quality by analyzing brightness and motion.
    Returns (is_valid, reason).
    """
    if not ENABLE_QUALITY_VALIDATION:
        return True, "Validation disabled"

    try:
        cap = cv2.VideoCapture(str(segment_path))
        if not cap.isOpened():
            return False, "Cannot open video"

        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        if frame_count < VALIDATION_FRAME_SAMPLES:
            cap.release()
            return False, "Too short"

        # Sample frames evenly throughout the video
        frame_indices = np.linspace(0, frame_count - 1, VALIDATION_FRAME_SAMPLES, dtype=int)
        brightness_values = []
        motion_scores = []
        prev_gray = None

        for idx in frame_indices:
            cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
            ret, frame = cap.read()
            if not ret:
                continue

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            brightness_values.append(gray.mean())

            # Calculate motion between consecutive samples
            if prev_gray is not None:
                diff = cv2.absdiff(prev_gray, gray)
                _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
                motion_percent = (np.count_nonzero(thresh) * 100) / thresh.size
                motion_scores.append(motion_percent)
            prev_gray = gray

        cap.release()

        # Validate brightness
        avg_brightness = np.mean(brightness_values)
        if not (MIN_BRIGHTNESS <= avg_brightness <= MAX_BRIGHTNESS):
            return False, f"Brightness out of range ({avg_brightness:.1f})"

        # Validate motion
        if motion_scores and np.mean(motion_scores) < MIN_MOTION_SCORE:
            return False, f"Insufficient motion ({np.mean(motion_scores):.2f})"

        return True, "OK"

    except Exception as e:
        return False, str(e)


def get_video_duration(video_path: Path) -> float:
    """Get video duration in seconds using ffmpeg."""
    result = subprocess.run(
        [FFMPEG_PATH, '-i', str(video_path)],
        capture_output=True, text=True, encoding='utf-8'
    )
    match = re.search(r"Duration: (\d{2}):(\d{2}):(\d{2}\.\d{2})", result.stderr)
    if match:
        hours, minutes, seconds = map(float, match.groups())
        return hours * 3600 + minutes * 60 + seconds
    return 0


def process_new_videos_into_segments():
    """
    Process all unprocessed raw videos into segments.
    Trims start/end if configured, then splits into fixed-length segments.
    """
    raw_dir = Path(RAW_VIDEOS_FOLDER)
    segments_dir = Path(SEGMENTS_FOLDER)
    segments_dir.mkdir(exist_ok=True)

    # Load processed video IDs
    processed_ids = set()
    if Path(PROCESSED_VIDEOS_LOG).exists():
        processed_ids = set(Path(PROCESSED_VIDEOS_LOG).read_text().splitlines())

    # Find unprocessed videos
    videos_to_process = [f for f in raw_dir.iterdir() if f.stem not in processed_ids and f.suffix == '.mp4']

    if not videos_to_process:
        logger.info("No new raw videos to process.")
        return

    for video_path in videos_to_process:
        logger.info(f"Processing: {video_path.name}")

        try:
            input_video = video_path

            # Trim video if enabled
            if ENABLE_VIDEO_TRIMMING:
                duration = get_video_duration(video_path)
                trimmed_duration = duration - TRIM_START_SECONDS - TRIM_END_SECONDS
                if trimmed_duration < SEGMENT_DURATION_SECONDS:
                    logger.warning(f"Video too short after trimming: {video_path.name}")
                    continue

                trimmed_path = raw_dir / f"{video_path.stem}_trimmed.mp4"
                subprocess.run([
                    FFMPEG_PATH, '-y',
                    '-ss', str(TRIM_START_SECONDS),
                    '-i', str(video_path),
                    '-t', str(trimmed_duration),
                    '-c', 'copy',
                    str(trimmed_path)
                ], capture_output=True)

                if trimmed_path.exists():
                    input_video = trimmed_path

            # Calculate segment count
            video_duration = get_video_duration(input_video)
            num_segments = math.floor(video_duration / SEGMENT_DURATION_SECONDS)

            logger.info(f"  -> Extracting {num_segments} segments...")

            for i in range(num_segments):
                segment_path = segments_dir / f"{video_path.stem}_seg{i+1}.mp4"
                start_time = i * SEGMENT_DURATION_SECONDS

                subprocess.run([
                    FFMPEG_PATH, '-y',
                    '-ss', str(start_time),
                    '-i', str(input_video),
                    '-t', str(SEGMENT_DURATION_SECONDS),
                    '-c', 'copy',
                    str(segment_path)
                ], capture_output=True)

                # Validate quality
                is_valid, reason = is_segment_high_quality(segment_path)
                if not is_valid:
                    segment_path.unlink()
                    logger.warning(f"  -> Segment {i+1} discarded: {reason}")
                else:
                    logger.info(f"  -> Segment {i+1} saved.")

            # Cleanup
            if input_video != video_path and input_video.exists():
                input_video.unlink()
            video_path.unlink()

            # Mark as processed
            with open(PROCESSED_VIDEOS_LOG, "a") as f:
                f.write(f"{video_path.stem}\n")

        except Exception as e:
            logger.error(f"Error processing {video_path.name}: {e}")
