"""
TTS Generator Module
--------------------
Text-to-Speech generation using Coqui TTS.
Supports voice cloning with gender-based voice samples.
"""

import torch
import logging
import random
from pathlib import Path
from TTS.api import TTS
from config import GENDER_VOICE_SAMPLES

logger = logging.getLogger(__name__)

# Device configuration
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
TTS_MODEL = None


def preload_coqui_models():
    """Pre-load TTS model into memory for faster generation."""
    global TTS_MODEL
    if not TTS_MODEL:
        TTS_MODEL = TTS(
            model_name="tts_models/multilingual/multi-dataset/xtts_v2",
            progress_bar=False
        ).to(DEVICE)
        logger.info("TTS Model loaded.")


def generate_audio(text: str, filename: str, gender: str) -> str:
    """
    Generate audio from text using voice cloning.

    Args:
        text: The script text to synthesize
        filename: Output file path
        gender: Narrator gender ('male', 'female', or 'neutral')

    Returns:
        The filename if successful, None otherwise
    """
    if not TTS_MODEL:
        return None

    # Select random voice from appropriate gender folder
    target_gender = random.choice(["male", "female"]) if gender == "neutral" else gender
    voice_folder = Path(GENDER_VOICE_SAMPLES[target_gender])
    wav_files = list(voice_folder.glob("*.wav"))

    if not wav_files:
        logger.error(f"No voice samples found in {voice_folder}")
        return None

    speaker_wav = str(random.choice(wav_files))
    logger.info(f"Using voice sample: {Path(speaker_wav).name}")

    try:
        TTS_MODEL.tts_to_file(
            text=text,
            speaker_wav=speaker_wav,
            language="es",  # Spanish output
            file_path=filename
        )
        return filename
    except Exception as e:
        logger.error(f"TTS Error: {e}")
        return None
