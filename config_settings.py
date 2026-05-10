import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
YOUTUBE_CHANNEL_ID = os.getenv('YOUTUBE_CHANNEL_ID')

# Social Media Tokens
LINKEDIN_TOKEN = os.getenv('LINKEDIN_ACCESS_TOKEN')
FACEBOOK_TOKEN = os.getenv('FACEBOOK_PAGE_TOKEN')
INSTAGRAM_ACCOUNT_ID = os.getenv('INSTAGRAM_BUSINESS_ACCOUNT_ID')
TWITTER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')

# Flask Settings
FLASK_ENV = os.getenv('FLASK_ENV', 'development')
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-change-in-production')
DEBUG = os.getenv('DEBUG', False) == 'True'

# Video Settings
VIDEO_OUTPUT_DIR = os.getenv('VIDEO_OUTPUT_DIR', 'videos')
SUBTITLE_LANGUAGE = os.getenv('SUBTITLE_LANGUAGE', 'hi-IN')
THUMBNAIL_SIZE = (1280, 720)
MAX_VIDEO_DURATION = 600  # 10 minutes in seconds

# Groq Model Settings
GROQ_MODEL = 'llama3-70b-8192'
MAX_TOKENS = 2048

# Supported Platforms
SUPPORTED_PLATFORMS = {
    'linkedin': 'LinkedIn',
    'facebook': 'Facebook',
    'instagram': 'Instagram',
    'twitter': 'Twitter/X',
    'youtube': 'YouTube'
}

# Video Styles
VIDEO_STYLES = {
    'educational': 'Educational & Informative',
    'entertainment': 'Entertainment & Fun',
    'vlog': 'Vlog Style',
    'motivational': 'Motivational & Inspiring',
    'tutorial': 'Tutorial & How-to'
}

# Languages
SUPPORTED_LANGUAGES = {
    'hi': 'Hindi',
    'en': 'English',
    'hi-en': 'Hinglish (Mix)'
}