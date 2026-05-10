"""
Production configuration for Flask app
"""

import os
from datetime import timedelta

class ProductionConfig:
    """Production configuration"""
    
    # Flask settings
    ENV = 'production'
    DEBUG = False
    TESTING = False
    
    # Security
    SECRET_KEY = os.getenv('SECRET_KEY', 'change-this-in-production')
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
    
    # CORS
    CORS_ORIGINS = ['https://yourdomain.com', 'https://app.yourdomain.com']
    
    # Logging
    LOG_LEVEL = 'INFO'
    LOG_FILE = 'logs/production.log'
    
    # Rate limiting
    RATELIMIT_ENABLED = True
    RATELIMIT_STORAGE_URL = 'memory://'
    
    # API
    JSON_SORT_KEYS = False
    JSONIFY_PRETTYPRINT_REGULAR = False

class DevelopmentConfig:
    """Development configuration"""
    
    ENV = 'development'
    DEBUG = True
    TESTING = False
    
    SECRET_KEY = 'dev-key-change-in-production'
    SESSION_COOKIE_SECURE = False
    
    LOG_LEVEL = 'DEBUG'
    
    RATELIMIT_ENABLED = False
    JSONIFY_PRETTYPRINT_REGULAR = True

# Export config
config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}