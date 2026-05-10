from flask import Blueprint, request, jsonify
from core.video_generator import VideoGenerator
from core.youtube_uploader import YouTubeUploader
from core.video_editor import VideoEditor
from datetime import datetime
import logging
import os

logger = logging.getLogger(__name__)
youtube_bp = Blueprint('youtube', __name__)

# Initialize generators and editors
video_gen = VideoGenerator()
video_editor = VideoEditor()

# YouTube uploader (lazy load - requires auth)
youtube_uploader = None

def get_uploader():
    """Get YouTube uploader instance"""
    global youtube_uploader
    if youtube_uploader is None:
        try:
            youtube_uploader = YouTubeUploader()
        except Exception as e:
            logger.error(f"Failed to initialize YouTube uploader: {str(e)}")
            return None
    return youtube_uploader

# ==================== SCRIPT GENERATION ====================

@youtube_bp.route('/script', methods=['POST'])
def generate_script():
    """Generate YouTube video script"""
    try:
        data = request.get_json()
        
        topic = data.get('topic')
        duration = data.get('duration', 5)
        style = data.get('style', 'educational')
        language = data.get('language', 'hindi')
        
        if not topic:
            return jsonify({'error': 'Topic is required'}), 400
        
        script = video_gen.generate_script(topic, duration, style, language)
        
        return jsonify({
            'success': True,
            'topic': topic,
            'duration': duration,
            'style': style,
            'language': language,
            'script': script,
            'generated_at': datetime.now().isoformat()
        })
    
    except Exception as e:
        logger.error(f"Error generating script: {str(e)}")
        return jsonify({'error': str(e)}), 500

@youtube_bp.route('/title', methods=['POST'])
def generate_title():
    """Generate YouTube video titles"""
    try:
        data = request.get_json()
        
        topic = data.get('topic')
        
        if not topic:
            return jsonify({'error': 'Topic is required'}), 400
        
        titles = video_gen.generate_title(topic)
        
        return jsonify({
            'success': True,
            'topic': topic,
            'titles': titles,
            'generated_at': datetime.now().isoformat()
        })
    
    except Exception as e:
        logger.error(f"Error generating titles: {str(e)}")
        return jsonify({'error': str(e)}), 500

@youtube_bp.route('/description', methods=['POST'])
def generate_description():
    """Generate YouTube video description"""
    try:
        data = request.get_json()
        
        topic = data.get('topic')
        duration = data.get('duration', 5)
        
        if not topic:
            return jsonify({'error': 'Topic is required'}), 400
        
        description = video_gen.generate_description(topic, duration)
        
        return jsonify({
            'success': True,
            'topic': topic,
            'duration': duration,
            'description': description,
            'generated_at': datetime.now().isoformat()
        })
    
    except Exception as e:
        logger.error(f"Error generating description: {str(e)}")
        return jsonify({'error': str(e)}), 500

@youtube_bp.route('/thumbnail-brief', methods=['POST'])
def thumbnail_brief():
    """Generate thumbnail design brief"""
    try:
        data = request.get_json()
        
        topic = data.get('topic')
        color = data.get('color', 'red')
        text = data.get('text', 'AI')
        
        if not topic:
            return jsonify({'error': 'Topic is required'}), 400
        
        brief = video_gen.generate_thumbnail_brief(topic, color, text)
        
        return jsonify({
            'success': True,
            'topic': topic,
            'color': color,
            'text': text,
            'brief': brief,
            'generated_at': datetime.now().isoformat()
        })
    
    except Exception as e:
        logger.error(f"Error generating thumbnail brief: {str(e)}")
        return jsonify({'error': str(e)}), 500

@youtube_bp.route('/full-package', methods=['POST'])
def full_package():
    """Generate complete video package (script + title + description)"""
    try:
        data = request.get_json()
        
        topic = data.get('topic')
        duration = data.get('duration', 5)
        
        if not topic:
            return jsonify({'error': 'Topic is required'}), 400
        
        package = video_gen.generate_full_video_package(topic, duration)
        
        return jsonify({
            'success': True,
            **package,
            'generated_at': datetime.now().isoformat()
        })
    
    except Exception as e:
        logger.error(f"Error generating full package: {str(e)}")
        return jsonify({'error': str(e)}), 500

# ==================== VIDEO EDITING ====================

@youtube_bp.route('/thumbnail', methods=['POST'])
def generate_thumbnail():
    """Generate YouTube thumbnail image"""
    try:
        data = request.get_json()
        
        title = data.get('title')
        subtitle = data.get('subtitle', '')
        color_str = data.get('color', 'red')
        
        if not title:
            return jsonify({'error': 'Title is required'}), 400
        
        # Convert color string to RGB tuple
        color_map = {
            'red': (255, 0, 0),
            'blue': (0, 0, 255),
            'green': (0, 255, 0),
            'yellow': (255, 255, 0),
            'orange': (255, 165, 0),
            'purple': (128, 0, 128),
            'black': (0, 0, 0),
            'white': (255, 255, 255)
        }
        
        color = color_map.get(color_str.lower(), (255, 0, 0))
        
        # Generate thumbnail
        output_path = video_editor.generate_thumbnail(title, subtitle, color)
        
        return jsonify({
            'success': True,
            'title': title,
            'subtitle': subtitle,
            'color': color_str,
            'output_path': output_path,
            'generated_at': datetime.now().isoformat()
        })
    
    except Exception as e:
        logger.error(f"Error generating thumbnail: {str(e)}")
        return jsonify({'error': str(e)}), 500

@youtube_bp.route('/subtitles', methods=['POST'])
def generate_subtitles():
    """Generate SRT subtitle file"""
    try:
        data = request.get_json()
        
        script = data.get('script')
        
        if not script:
            return jsonify({'error': 'Script is required'}), 400
        
        output_path = video_editor.generate_subtitle_file(script)
        
        return jsonify({
            'success': True,
            'script_length': len(script),
            'output_path': output_path,
            'generated_at': datetime.now().isoformat()
        })
    
    except Exception as e:
        logger.error(f"Error generating subtitles: {str(e)}")
        return jsonify({'error': str(e)}), 500

# ==================== YOUTUBE UPLOAD ====================

@youtube_bp.route('/upload', methods=['POST'])
def upload_video():
    """Upload video to YouTube"""
    try:
        uploader = get_uploader()
        if not uploader:
            return jsonify({
                'error': 'YouTube authentication failed',
                'message': 'Please configure YouTube credentials'
            }), 401
        
        data = request.get_json()
        
        video_path = data.get('video_path')
        title = data.get('title')
        description = data.get('description')
        tags = data.get('tags', [])
        is_public = data.get('is_public', False)
        schedule_time = data.get('schedule_time')
        
        if not video_path or not title:
            return jsonify({'error': 'video_path and title are required'}), 400
        
        result = uploader.upload_video(
            video_path, title, description, tags, 
            is_public=is_public, schedule_time=schedule_time
        )
        
        if 'error' in result:
            return jsonify(result), 500
        
        return jsonify({
            'success': True,
            **result,
            'uploaded_at': datetime.now().isoformat()
        })
    
    except Exception as e:
        logger.error(f"Error uploading video: {str(e)}")
        return jsonify({'error': str(e)}), 500

@youtube_bp.route('/update/<video_id>', methods=['PUT'])
def update_video(video_id):
    """Update video metadata"""
    try:
        uploader = get_uploader()
        if not uploader:
            return jsonify({'error': 'YouTube authentication failed'}), 401
        
        data = request.get_json()
        
        result = uploader.update_video(
            video_id,
            title=data.get('title'),
            description=data.get('description'),
            tags=data.get('tags')
        )
        
        if 'error' in result:
            return jsonify(result), 500
        
        return jsonify({
            'success': True,
            **result
        })
    
    except Exception as e:
        logger.error(f"Error updating video: {str(e)}")
        return jsonify({'error': str(e)}), 500

@youtube_bp.route('/stats/<video_id>', methods=['GET'])
def get_video_stats(video_id):
    """Get video statistics"""
    try:
        uploader = get_uploader()
        if not uploader:
            return jsonify({'error': 'YouTube authentication failed'}), 401
        
        result = uploader.get_video_stats(video_id)
        
        if 'error' in result:
            return jsonify(result), 500
        
        return jsonify({
            'success': True,
            **result
        })
    
    except Exception as e:
        logger.error(f"Error getting video stats: {str(e)}")
        return jsonify({'error': str(e)}), 500

@youtube_bp.route('/schedule', methods=['POST'])
def schedule_video():
    """Schedule video for publishing"""
    try:
        uploader = get_uploader()
        if not uploader:
            return jsonify({'error': 'YouTube authentication failed'}), 401
        
        data = request.get_json()
        
        video_id = data.get('video_id')
        publish_time = data.get('publish_time')
        
        if not video_id or not publish_time:
            return jsonify({'error': 'video_id and publish_time are required'}), 400
        
        result = uploader.schedule_video(video_id, publish_time)
        
        if 'error' in result:
            return jsonify(result), 500
        
        return jsonify({
            'success': True,
            **result
        })
    
    except Exception as e:
        logger.error(f"Error scheduling video: {str(e)}")
        return jsonify({'error': str(e)}), 500

# ==================== PLAYLIST MANAGEMENT ====================

@youtube_bp.route('/playlist/create', methods=['POST'])
def create_playlist():
    """Create a new playlist"""
    try:
        uploader = get_uploader()
        if not uploader:
            return jsonify({'error': 'YouTube authentication failed'}), 401
        
        data = request.get_json()
        
        title = data.get('title')
        description = data.get('description', '')
        is_public = data.get('is_public', False)
        
        if not title:
            return jsonify({'error': 'Title is required'}), 400
        
        result = uploader.create_playlist(title, description, is_public)
        
        if 'error' in result:
            return jsonify(result), 500
        
        return jsonify({
            'success': True,
            **result
        })
    
    except Exception as e:
        logger.error(f"Error creating playlist: {str(e)}")
        return jsonify({'error': str(e)}), 500

@youtube_bp.route('/playlist/<playlist_id>/add', methods=['POST'])
def add_to_playlist(playlist_id):
    """Add video to playlist"""
    try:
        uploader = get_uploader()
        if not uploader:
            return jsonify({'error': 'YouTube authentication failed'}), 401
        
        data = request.get_json()
        
        video_id = data.get('video_id')
        
        if not video_id:
            return jsonify({'error': 'video_id is required'}), 400
        
        result = uploader.add_video_to_playlist(playlist_id, video_id)
        
        if 'error' in result:
            return jsonify(result), 500
        
        return jsonify({
            'success': True,
            **result
        })
    
    except Exception as e:
        logger.error(f"Error adding video to playlist: {str(e)}")
        return jsonify({'error': str(e)}), 500

# ==================== UTILITIES ====================

@youtube_bp.route('/styles', methods=['GET'])
def get_styles():
    """Get available video styles"""
    styles = {
        'educational': 'Educational & Informative',
        'entertainment': 'Entertainment & Fun',
        'vlog': 'Vlog Style',
        'motivational': 'Motivational & Inspiring',
        'tutorial': 'Tutorial & How-to'
    }
    return jsonify({'success': True, 'styles': styles})

@youtube_bp.route('/languages', methods=['GET'])
def get_languages():
    """Get supported languages"""
    languages = {
        'hindi': 'हिंदी',
        'english': 'English',
        'hinglish': 'Hinglish'
    }
    return jsonify({'success': True, 'languages': languages})

@youtube_bp.route('/categories', methods=['GET'])
def get_categories():
    """Get YouTube categories"""
    categories = {
        '22': 'People & Blogs',
        '27': 'Education',
        '24': 'Entertainment',
        '26': 'Howto & Style',
        '23': 'Comedy',
        '20': 'Gaming'
    }
    return jsonify({'success': True, 'categories': categories})