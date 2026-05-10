from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
from datetime import datetime
import traceback

app = Flask(__name__)
CORS(app)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Health check
@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'Prashant Social AI Bot'
    })

# Version
@app.route('/version', methods=['GET'])
def version():
    """Get API version"""
    return jsonify({
        'version': '1.0.0',
        'release_date': '2026-05-10',
        'features': [
            'Social Media Posts',
            'YouTube Content',
            'Video Editing',
            'Auto Scheduling'
        ]
    })

# Info
@app.route('/info', methods=['GET'])
def info():
    """Get API information"""
    return jsonify({
        'name': 'Prashant Social AI Bot',
        'description': 'AI-powered social media and YouTube content creator',
        'author': 'Prashant',
        'organization': 'PB Partners',
        'supported_platforms': [
            'LinkedIn', 'Facebook', 'Instagram', 'Twitter/X', 'YouTube'
        ],
        'api_endpoints': {
            'social': '/api/social/*',
            'youtube': '/api/youtube/*'
        }
    })

# Import route blueprints
from api.social_routes import social_bp
from api.youtube_routes import youtube_bp

# Register blueprints
app.register_blueprint(social_bp, url_prefix='/api/social')
app.register_blueprint(youtube_bp, url_prefix='/api/youtube')

# Error handler
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'error': 'Endpoint not found',
        'message': str(error)
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    logger.error(f"Internal error: {traceback.format_exc()}")
    return jsonify({
        'error': 'Internal server error',
        'message': 'An unexpected error occurred'
    }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)