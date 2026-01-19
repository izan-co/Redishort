"""
Video Downloader Module
-----------------------
Downloads background videos from curated YouTube channels.
Uses a tiered hunting system to find suitable long-form content.
"""

import random
import time
import yt_dlp
import logging
from pathlib import Path
from config import (
    RAW_VIDEOS_FOLDER, PROCESSED_VIDEOS_LOG, YOUTUBE_COOKIES_FILE,
    MAX_RAW_VIDEOS_IN_LIBRARY, CHANNEL_SCAN_LIMIT, HUNTING_TIERS,
    CURATED_CHANNEL_IDS, ENABLE_VIDEO_TRIMMING, TRIM_START_SECONDS, TRIM_END_SECONDS
)

logger = logging.getLogger(__name__)


def download_new_source_videos(num_to_download: int):
    """
    Download new source videos from curated channels.
    Uses a tiered approach: tries to find longest videos first.
    """
    Path(RAW_VIDEOS_FOLDER).mkdir(exist_ok=True)

    # Load processed video IDs
    processed_ids = set()
    if Path(PROCESSED_VIDEOS_LOG).exists():
        processed_ids = set(Path(PROCESSED_VIDEOS_LOG).read_text().splitlines())

    downloaded = []
    channels = random.sample(CURATED_CHANNEL_IDS, len(CURATED_CHANNEL_IDS))

    for tier in HUNTING_TIERS:
        if len(downloaded) >= num_to_download:
            break

        min_duration = tier["min_duration_seconds"]
        if ENABLE_VIDEO_TRIMMING:
            min_duration += TRIM_START_SECONDS + TRIM_END_SECONDS

        logger.info(f"--- Hunting Tier: '{tier['tier_name']}' (Min Duration: {min_duration/60:.1f}m) ---")

        # Collect candidates from all channels
        candidates = []
        for channel_id in channels:
            try:
                ydl_opts = {
                    'extract_flat': True,
                    'quiet': True,
                    'playlistend': CHANNEL_SCAN_LIMIT
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    channel_url = f"https://www.youtube.com/channel/{channel_id}/videos"
                    info = ydl.extract_info(channel_url, download=False)

                for video in info.get('entries', []):
                    if not video:
                        continue
                    duration = video.get('duration', 0)
                    video_id = video.get('id')
                    if duration > min_duration and video_id not in processed_ids:
                        candidates.append(video)
            except Exception as e:
                logger.debug(f"Failed to scan channel {channel_id}: {e}")
                continue

        # Shuffle and download
        random.shuffle(candidates)
        for video in candidates:
            if len(downloaded) >= num_to_download:
                break

            video_id = video['id']
            output_path = Path(RAW_VIDEOS_FOLDER) / f"{video_id}.mp4"
            logger.info(f"    -> Trying: '{video.get('title', 'Unknown')[:50]}...'")

            download_opts = {
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio/best',
                'outtmpl': str(output_path),
                'quiet': True,
                'merge_output_format': 'mp4',
            }
            if Path(YOUTUBE_COOKIES_FILE).exists():
                download_opts['cookiefile'] = str(YOUTUBE_COOKIES_FILE)

            try:
                with yt_dlp.YoutubeDL(download_opts) as ydl:
                    ydl.download([f"https://www.youtube.com/watch?v={video_id}"])

                if output_path.exists() and output_path.stat().st_size > 1024:
                    downloaded.append(str(output_path))
                    processed_ids.add(video_id)
                    logger.info("    -> ✅ Download success.")
                else:
                    logger.warning("    -> ❌ Download resulted in empty file.")
            except Exception as e:
                logger.warning(f"    -> ❌ Download failed: {e}")

            # Rate limiting to avoid YouTube throttling
            time.sleep(random.uniform(60, 120))

    # Save processed IDs
    if processed_ids:
        with open(PROCESSED_VIDEOS_LOG, "w") as f:
            f.write("\n".join(processed_ids))

    logger.info(f"Download session complete. {len(downloaded)} videos downloaded.")
