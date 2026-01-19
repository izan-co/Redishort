# Central Configuration Module
# -------------------------------
# This file acts as the control panel for the entire application.
# It contains all variables and parameters defining the bot's behavior,
# from scheduling to video aesthetic details.

import os
from pathlib import Path

# --- 1. General Publishing Configuration ---
TIMEZONE = "Europe/Madrid"
PUBLISHING_SCHEDULE = [  # Time of day (24h format) to attempt publishing.
    "08:00",
    "10:30",  # Test run
    "13:00",
    "18:00",
    "20:00",
    "22:00",
]
PUBLISH_TOLERANCE_MINUTES = 30  # Margin (in minutes) to decide whether to publish immediately or reschedule.
YOUTUBE_VIDEO_CATEGORY_ID = "24"  # YouTube Category ID ("Entertainment").

# --- 2. Asset Library Management ---
MIN_SEGMENTS_IN_LIBRARY = 10  # Maintenance cycle triggers if ready-to-use segments fall below this.

# --- 3. Core Directories ---
BASE_DIR = Path(__file__).parent.absolute()
ASSETS_FOLDER = BASE_DIR / "assets"
RAW_VIDEOS_FOLDER = ASSETS_FOLDER / "raw_videos"
SEGMENTS_FOLDER = ASSETS_FOLDER / "segments"
SESSIONS_FOLDER = ASSETS_FOLDER / "sessions"
OUTPUT_FOLDER = BASE_DIR / "ready_to_upload"

# --- 4. Logs and Memory ---
PROCESSED_POSTS_FILE = BASE_DIR / "processed_posts.txt"
PROCESSED_VIDEOS_LOG = BASE_DIR / "processed_raw_videos.txt"

# --- 5. Business Logic Parameters ---
MAX_STORIES_PER_RUN = 1
MAX_SCRIPT_WORD_COUNT = 145

# --- 6. Coqui TTS Voice Config ---
VOICE_SAMPLES_BASE_FOLDER = ASSETS_FOLDER / "voice_samples"
GENDER_VOICE_SAMPLES = {
    "male": str(VOICE_SAMPLES_BASE_FOLDER / "male"),
    "female": str(VOICE_SAMPLES_BASE_FOLDER / "female"),
}

# --- 7. Reddit Hunter Parameters ---
NUM_HOT_SUBREDDITS_TO_HUNT = 30
MIN_POST_TEXT_LENGTH = 80
MIN_COMMENT_TEXT_LENGTH = 25
POST_SCORE_WEIGHT = 1.0
COMMENT_SCORE_WEIGHT = 1.0
ALL_SUBREDDITS = [
    "AmItheAsshole", "AITAH", "AmItheButtface", "AmITheDevil", "AmItheJerk",
    "TrueOffMyChest", "offmychest", "confession", "confessions", "Desahogo",
    "self", "Vent", "venting", "rant", "cuentaleareddit", "stories",
    "CrazyFuckingStories", "ThatHappened", "relationship_advice", "relationships",
    "dating_advice", "relaciones", "JustNoMIL", "JUSTNOFAMILY", "weddingdrama",
    "bridezillas", "stepparents", "raisedbynarcissists", "breakups", "divorce",
    "datinghell", "ProRevenge", "MaliciousCompliance", "pettyrevenge",
    "NuclearRevenge", "talesfromretail", "TalesFromYourServer",
    "TalesFromTechSupport", "TalesFromTheCustomer", "TalesFromTheFrontDesk",
    "TalesFromCallCenters", "TalesFromSecurity", "talesfromHR", "ITdept",
    "IDontWorkHereLady", "antiwork", "workreform", "recruitinghell", "tifu",
    "AskReddit", "AskRedditespanol", "AskMen", "AskWomen", "TooAfraidToAsk",
    "legaladvice", "BestofLegalAdvice", "legaladviceofftopic", "esLegal",
    "entitledparents", "entitledpeople", "EntitledKarens", "nosleep",
    "LetsNotMeet", "creepyencounters", "Paranormal", "Glitch_in_the_Matrix",
    "ScaryStories", "UnresolvedMysteries", "unpopularopinion",
    "TrueUnpopularOpinion", "The10thDentist", "Showerthoughts", "TodayILearned",
    "nottheonion", "ExplainLikeImFive", "AskScience", "AskHistorians",
    "espanol", "Mexico", "es", "Colombia", "argentina", "chile", "PERU",
    "BestofRedditorUpdates"
]

# --- 8. Video Pre-processing and Download ---
ENABLE_VIDEO_TRIMMING = True
TRIM_START_SECONDS = 30
TRIM_END_SECONDS = 30
MAX_RAW_VIDEOS_IN_LIBRARY = 6
CHANNEL_SCAN_LIMIT = 50
HUNTING_TIERS = [
    {"tier_name": "Ideal (Over 45m)", "min_duration_seconds": 2700},
    {"tier_name": "Acceptable (Over 20m)", "min_duration_seconds": 1200},
    {"tier_name": "Minimum (Over 10m)", "min_duration_seconds": 600},
]
CURATED_CHANNEL_IDS = [
    "UC7eAfUjR9gdIjoaoQaS0W-A", "UCMlSf7BCzfdRsIGAIpCnrXA", "UCxFQofXJq9WxWWqlsTiQ-Aw",
    "UCns4T9U8VSIRovKa1a_r7rA", "UCTSg06MQbQ5j3slP4mjzUEg", "UCERExzbCGBxhhWBtFnMLInA",
    "UC4r6nalq_1-9rc80qdVLatQ", "UCB5POybzno8F7lwLEr_C8og", "UCCZIevhN62jJ2gb-u__M95g",
    "UCSNIT8Z40XgB4RKk9Vhf1eA", "UCrI3dm4qgAEV67Jc6797WIA", "UCIGEtjevANE0Nqain3EqNSg",
    "UCTGjE7hWuBRNqU-OnVSzq3Q", "UCEoEkMVF0b_9SUnJaThEYRA", "UChgkHw9M_OUTjYtFqkA1WOQ",
]

# --- 9. Segmenter and Assembler Parameters ---
SEGMENT_DURATION_SECONDS = 120
WHISPER_MODEL = "base"

# --- 10. External Tools ---
YOUTUBE_COOKIES_FILE = BASE_DIR / "cookies.txt"
FFMPEG_PATH = "ffmpeg"
IMAGEMAGICK_PATH = "/usr/bin/convert"

# --- 11. Rendering and Subtitles ---
VIDEO_RESOLUTION = (1080, 1920)
VIDEO_FPS = 30
VIDEO_BITRATE = "8000k"
AUDIO_BITRATE = "192k"
VIDEO_PRESET = "superfast"
ASPECT_RATIO = 9 / 16
SUBTITLE_FONT = "/app/assets/fonts/Anton-Regular.ttf"
SUBTITLE_FONTSIZE = 138
SUBTITLE_COLOR = "#FFFFFF"
SUBTITLE_STROKE_COLORS = {
    "male": "#FF4500",
    "female": "#49B6C2",
    "neutral": "#000000"
}
SUBTITLE_STROKE_WIDTH = 14
SUBTITLE_SHADOW_COLOR = "#000000B3"
SUBTITLE_SHADOW_OFFSET = 6

# --- 12. Cleanup Management ---
MAX_SESSIONS_TO_KEEP = 5
MIN_SEGMENT_SIZE_BYTES = 102400

# --- 13. Quality Validation ---
ENABLE_QUALITY_VALIDATION = True
VALIDATION_FRAME_SAMPLES = 5
MIN_BRIGHTNESS = 30
MAX_BRIGHTNESS = 220
MIN_MOTION_SCORE = 1.0

# --- 14. AI Providers (LLM) ---
LLM_PROVIDERS = [
    {
        "name": "gemini",
        "model": "gemini-3-flash-preview",
        "api_key_env": "GOOGLE_API_KEY"
    },
    {
        "name": "gemini",
        "model": "gemini-2.5-flash",
        "api_key_env": "GOOGLE_API_KEY"
    }
]
