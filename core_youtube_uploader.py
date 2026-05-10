import os
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from config.settings import YOUTUBE_API_KEY, YOUTUBE_CHANNEL_ID
from datetime import datetime, timedelta

class YouTubeUploader:
    def __init__(self):
        """Initialize YouTube uploader"""
        self.SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
        self.SERVICE_NAME = 'youtube'
        self.API_VERSION = 'v3'
        self.youtube = None
        self.credentials = None
        self.authenticate()
    
    def authenticate(self):
        """Authenticate with YouTube API"""
        credentials_file = 'youtube_credentials.pickle'
        
        # Try to load existing credentials
        if os.path.exists(credentials_file):
            with open(credentials_file, 'rb') as token:
                self.credentials = pickle.load(token)
        
        # If credentials don't exist or are invalid, create new ones
        if not self.credentials or not self.credentials.valid:
            if self.credentials and self.credentials.expired and self.credentials.refresh_token:
                self.credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'client_secret.json', self.SCOPES)
                self.credentials = flow.run_local_server(port=0)
            
            # Save credentials for future use
            with open(credentials_file, 'wb') as token:
                pickle.dump(self.credentials, token)
        
        self.youtube = build(self.SERVICE_NAME, self.API_VERSION, 
                            credentials=self.credentials)
    
    def upload_video(self, video_path: str, title: str, description: str,
                     tags: list = None, category_id: str = '22',
                     is_public: bool = False, schedule_time: str = None) -> dict:
        """
        Upload video to YouTube
        
        Args:
            video_path: Path to video file
            title: Video title
            description: Video description
            tags: List of tags/hashtags
            category_id: YouTube category ID (22 = People & Blogs)
            is_public: Whether video is public
            schedule_time: Schedule publish time (ISO format)
            
        Returns:
            Upload response with video ID
        """
        if not os.path.exists(video_path):
            return {'error': f'Video file not found: {video_path}'}
        
        try:
            # Prepare request body
            body = {
                'snippet': {
                    'title': title,
                    'description': description,
                    'tags': tags or ['PrashantAI', 'PBPartners'],
                    'categoryId': category_id
                },
                'status': {
                    'privacyStatus': 'public' if is_public else 'private',
                    'selfDeclaredMadeForKids': False,
                }
            }
            
            # Add schedule time if provided
            if schedule_time:
                body['status']['publishAt'] = schedule_time
            
            # Upload video
            media = MediaFileUpload(video_path, chunksize=-1, resumable=True)
            
            request = self.youtube.videos().insert(
                part='snippet,status',
                body=body,
                media_body=media
            )
            
            response = request.execute()
            
            return {
                'success': True,
                'video_id': response['id'],
                'url': f"https://www.youtube.com/watch?v={response['id']}",
                'status': response['status']['privacyStatus']
            }
        
        except Exception as e:
            return {'error': str(e)}
    
    def update_video(self, video_id: str, title: str = None, 
                    description: str = None, tags: list = None) -> dict:
        """
        Update existing video metadata
        
        Args:
            video_id: YouTube video ID
            title: New title
            description: New description
            tags: New tags
            
        Returns:
            Update response
        """
        try:
            # Get current video details
            request = self.youtube.videos().list(
                part='snippet',
                id=video_id
            )
            response = request.execute()
            
            if not response['items']:
                return {'error': 'Video not found'}
            
            video = response['items'][0]
            snippet = video['snippet']
            
            # Update fields
            if title:
                snippet['title'] = title
            if description:
                snippet['description'] = description
            if tags:
                snippet['tags'] = tags
            
            # Update video
            update_request = self.youtube.videos().update(
                part='snippet',
                body={'id': video_id, 'snippet': snippet}
            )
            
            update_response = update_request.execute()
            
            return {
                'success': True,
                'video_id': update_response['id'],
                'updated_at': datetime.now().isoformat()
            }
        
        except Exception as e:
            return {'error': str(e)}
    
    def get_video_stats(self, video_id: str) -> dict:
        """
        Get video statistics
        
        Args:
            video_id: YouTube video ID
            
        Returns:
            Video statistics
        """
        try:
            request = self.youtube.videos().list(
                part='statistics,snippet',
                id=video_id
            )
            response = request.execute()
            
            if not response['items']:
                return {'error': 'Video not found'}
            
            video = response['items'][0]
            stats = video['statistics']
            
            return {
                'video_id': video_id,
                'title': video['snippet']['title'],
                'views': int(stats.get('viewCount', 0)),
                'likes': int(stats.get('likeCount', 0)),
                'comments': int(stats.get('commentCount', 0)),
                'shares': int(stats.get('shareCount', 0))
            }
        
        except Exception as e:
            return {'error': str(e)}
    
    def create_playlist(self, title: str, description: str = '',
                       is_public: bool = False) -> dict:
        """
        Create a new playlist
        
        Args:
            title: Playlist title
            description: Playlist description
            is_public: Whether playlist is public
            
        Returns:
            Playlist creation response
        """
        try:
            body = {
                'snippet': {
                    'title': title,
                    'description': description
                },
                'status': {
                    'privacyStatus': 'public' if is_public else 'private'
                }
            }
            
            request = self.youtube.playlists().insert(
                part='snippet,status',
                body=body
            )
            
            response = request.execute()
            
            return {
                'success': True,
                'playlist_id': response['id'],
                'url': f"https://www.youtube.com/playlist?list={response['id']}"
            }
        
        except Exception as e:
            return {'error': str(e)}
    
    def add_video_to_playlist(self, playlist_id: str, video_id: str) -> dict:
        """
        Add video to playlist
        
        Args:
            playlist_id: Playlist ID
            video_id: Video ID to add
            
        Returns:
            Response
        """
        try:
            body = {
                'snippet': {
                    'playlistId': playlist_id,
                    'resourceId': {
                        'kind': 'youtube#video',
                        'videoId': video_id
                    }
                }
            }
            
            request = self.youtube.playlistItems().insert(
                part='snippet',
                body=body
            )
            
            response = request.execute()
            
            return {
                'success': True,
                'item_id': response['id']
            }
        
        except Exception as e:
            return {'error': str(e)}
    
    def schedule_video(self, video_id: str, publish_time: str) -> dict:
        """
        Schedule video for future publication
        
        Args:
            video_id: Video ID
            publish_time: ISO format datetime string
            
        Returns:
            Response
        """
        try:
            request = self.youtube.videos().list(
                part='status',
                id=video_id
            )
            response = request.execute()
            
            if not response['items']:
                return {'error': 'Video not found'}
            
            video = response['items'][0]
            video['status']['publishAt'] = publish_time
            video['status']['privacyStatus'] = 'scheduled'
            
            update_request = self.youtube.videos().update(
                part='status',
                body=video
            )
            
            update_response = update_request.execute()
            
            return {
                'success': True,
                'scheduled_at': publish_time
            }
        
        except Exception as e:
            return {'error': str(e)}