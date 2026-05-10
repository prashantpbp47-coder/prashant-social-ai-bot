# YouTube Category IDs
YOUTUBE_CATEGORIES = {
    '1': 'Film & Animation',
    '2': 'Autos & Vehicles',
    '10': 'Music',
    '15': 'Pets & Animals',
    '17': 'Sports',
    '18': 'Short Movies',
    '19': 'Travel & Events',
    '20': 'Gaming',
    '21': 'Videoblogging',
    '22': 'People & Blogs',  # Most common for creators
    '23': 'Comedy',
    '24': 'Entertainment',
    '25': 'News & Politics',
    '26': 'Howto & Style',
    '27': 'Education',
    '28': 'Science & Technology',
    '29': 'Nonprofits & Activism',
    '30': 'Movies',
    '31': 'Anime/Animation',
    '32': 'Action/Adventure',
    '33': 'Classics',
    '34': 'Comedies',
    '35': 'Documentaries',
    '36': 'Dramas',
    '37': 'Family',
    '38': 'Foreign',
    '39': 'Horror',
    '40': 'Sci-Fi/Fantasy',
    '41': 'Thrillers',
    '42': 'Shorts',
    '43': 'Shows',
    '44': 'Trailers'
}

# Default settings for YouTube uploads
DEFAULT_UPLOAD_CONFIG = {
    'category_id': '22',  # People & Blogs
    'is_public': False,   # Private by default
    'made_for_kids': False,
    'allow_comments': True,
    'allow_ratings': True,
    'embeddable': True,
}

# Video quality recommendations
VIDEO_QUALITY = {
    '360p': {'width': 640, 'height': 360, 'fps': 30},
    '480p': {'width': 854, 'height': 480, 'fps': 30},
    '720p': {'width': 1280, 'height': 720, 'fps': 30},
    '1080p': {'width': 1920, 'height': 1080, 'fps': 60},
    '4K': {'width': 3840, 'height': 2160, 'fps': 60},
}

# Recommended video formats
VIDEO_FORMATS = {
    'codec': 'h264',
    'audio_codec': 'aac',
    'bitrate_video': '5000k',  # 5 Mbps
    'bitrate_audio': '128k',   # 128 kbps
}

# Thumbnail settings
THUMBNAIL_CONFIG = {
    'width': 1280,
    'height': 720,
    'min_width': 640,
    'min_height': 360,
    'format': 'jpg',
    'max_size_mb': 2,
}

# Allowed file formats for upload
ALLOWED_VIDEO_FORMATS = [
    'mov', 'mpeg4', 'mp4', 'mpg', 'avi', 'wmv', 
    'flv', '3gp', 'ogv', 'ts', 'f4v', 'webm'
]

ALLOWED_THUMBNAIL_FORMATS = ['jpg', 'jpeg', 'png', 'gif', 'bmp']

# Video upload size limits
MAX_VIDEO_SIZE_GB = 256
MAX_UPLOAD_DURATION_HOURS = 12

# API rate limits
API_RATE_LIMIT = {
    'requests_per_second': 1,
    'quota_per_day': 10000,
    'uploads_per_day': 50
}

# Recommended video lengths for different content
RECOMMENDED_DURATION = {
    'short_form': (15, 60),        # 15-60 seconds (YouTube Shorts)
    'medium': (3, 10),             # 3-10 minutes
    'long_form': (15, 60),         # 15-60 minutes
    'educational': (5, 15),        # 5-15 minutes
    'vlog': (5, 20),               # 5-20 minutes
    'tutorial': (10, 30),          # 10-30 minutes
}

# SEO settings
SEO_CONFIG = {
    'min_title_length': 30,
    'max_title_length': 100,
    'recommended_tags': 10,
    'min_description_length': 100,
    'max_description_length': 5000,
}