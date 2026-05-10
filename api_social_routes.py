from flask import Blueprint, request, jsonify
from core.post_generator import PostGenerator
from datetime import datetime
import logging

logger = logging.getLogger(__name__)
social_bp = Blueprint('social', __name__)

# Initialize generator
post_gen = PostGenerator()

@social_bp.route('/generate', methods=['POST'])
def generate_post():
    """Generate a social media post"""
    try:
        data = request.get_json()
        
        topic = data.get('topic')
        platform = data.get('platform', 'linkedin')
        language = data.get('language', 'hindi')
        style = data.get('style', 'professional')
        
        if not topic:
            return jsonify({'error': 'Topic is required'}), 400
        
        post = post_gen.generate_post(topic, platform, language, style)
        
        return jsonify({
            'success': True,
            'topic': topic,
            'platform': platform,
            'language': language,
            'style': style,
            'content': post,
            'generated_at': datetime.now().isoformat()
        })
    
    except Exception as e:
        logger.error(f"Error generating post: {str(e)}")
        return jsonify({'error': str(e)}), 500

@social_bp.route('/generate-bulk', methods=['POST'])
def generate_bulk():
    """Generate posts for multiple topics"""
    try:
        data = request.get_json()
        
        topics = data.get('topics', [])
        platform = data.get('platform', 'linkedin')
        
        if not topics:
            return jsonify({'error': 'Topics list is required'}), 400
        
        posts = post_gen.generate_bulk_posts(topics, platform)
        
        return jsonify({
            'success': True,
            'platform': platform,
            'count': len(posts),
            'posts': posts,
            'generated_at': datetime.now().isoformat()
        })
    
    except Exception as e:
        logger.error(f"Error generating bulk posts: {str(e)}")
        return jsonify({'error': str(e)}), 500

@social_bp.route('/with-hashtags', methods=['POST'])
def generate_with_hashtags():
    """Generate post with hashtags"""
    try:
        data = request.get_json()
        
        topic = data.get('topic')
        platform = data.get('platform', 'linkedin')
        
        if not topic:
            return jsonify({'error': 'Topic is required'}), 400
        
        result = post_gen.generate_with_hashtags(topic, platform)
        
        return jsonify({
            'success': True,
            'topic': topic,
            'platform': platform,
            'content': result['content'],
            'hashtags': result['hashtags'],
            'generated_at': datetime.now().isoformat()
        })
    
    except Exception as e:
        logger.error(f"Error generating post with hashtags: {str(e)}")
        return jsonify({'error': str(e)}), 500

@social_bp.route('/platforms', methods=['GET'])
def get_platforms():
    """Get list of supported platforms"""
    platforms = {
        'linkedin': {'name': 'LinkedIn', 'character_limit': 3000},
        'facebook': {'name': 'Facebook', 'character_limit': 63206},
        'instagram': {'name': 'Instagram', 'character_limit': 2200},
        'twitter': {'name': 'Twitter/X', 'character_limit': 280},
    }
    return jsonify({
        'success': True,
        'platforms': platforms
    })

@social_bp.route('/languages', methods=['GET'])
def get_languages():
    """Get list of supported languages"""
    languages = {
        'hindi': 'हिंदी',
        'english': 'English',
        'hinglish': 'Hinglish (हिंग्लिश)'
    }
    return jsonify({
        'success': True,
        'languages': languages
    })

@social_bp.route('/styles', methods=['GET'])
def get_styles():
    """Get list of writing styles"""
    styles = {
        'professional': 'Professional & Business',
        'casual': 'Casual & Friendly',
        'motivational': 'Motivational & Inspiring',
        'entertaining': 'Entertaining & Fun',
        'educational': 'Educational & Informative'
    }
    return jsonify({
        'success': True,
        'styles': styles
    })