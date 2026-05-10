from core.groq_client import GroqClient
from config.prompts import (
    YOUTUBE_SCRIPT_PROMPT, YOUTUBE_TITLE_PROMPT,
    YOUTUBE_DESCRIPTION_PROMPT, THUMBNAIL_PROMPT
)
import json

class VideoGenerator:
    def __init__(self):
        """Initialize video generator"""
        self.groq = GroqClient()
    
    def generate_script(self, topic: str, duration: int = 5, 
                       style: str = 'educational', language: str = 'hindi') -> str:
        """
        Generate YouTube video script
        
        Args:
            topic: Video topic
            duration: Video duration in minutes
            style: Video style (educational, entertainment, vlog, etc.)
            language: Language (hindi, english, hinglish)
            
        Returns:
            Generated video script
        """
        main_duration = max(0, duration * 60 - 90)  # Subtract hook, intro, outro
        
        prompt = YOUTUBE_SCRIPT_PROMPT.format(
            duration=duration,
            topic=topic,
            style=style,
            language=language,
            main_duration=main_duration
        )
        
        return self.groq.generate_text(prompt, temperature=0.8)
    
    def generate_title(self, topic: str) -> list:
        """
        Generate YouTube video titles
        
        Args:
            topic: Video topic
            
        Returns:
            List of title suggestions
        """
        prompt = YOUTUBE_TITLE_PROMPT.format(topic=topic)
        response = self.groq.generate_text(prompt)
        
        # Parse titles from response
        titles = []
        for line in response.split('\n'):
            line = line.strip()
            if line and not line.startswith('**'):
                titles.append(line.lstrip('0123456789.-) '))
        
        return titles[:5]
    
    def generate_description(self, topic: str, duration: int = 5) -> str:
        """
        Generate YouTube video description
        
        Args:
            topic: Video topic
            duration: Video duration in minutes
            
        Returns:
            Generated description
        """
        prompt = YOUTUBE_DESCRIPTION_PROMPT.format(
            topic=topic,
            duration=duration
        )
        
        return self.groq.generate_text(prompt)
    
    def generate_thumbnail_brief(self, topic: str, color: str = 'red', 
                                text: str = 'AI') -> str:
        """
        Generate thumbnail design brief
        
        Args:
            topic: Video topic
            color: Main color for thumbnail
            text: Main text for thumbnail
            
        Returns:
            Design brief for thumbnail
        """
        prompt = THUMBNAIL_PROMPT.format(
            topic=topic,
            color=color,
            text=text
        )
        
        return self.groq.generate_text(prompt)
    
    def generate_full_video_package(self, topic: str, duration: int = 5) -> dict:
        """
        Generate complete video package (script, title, description)
        
        Args:
            topic: Video topic
            duration: Video duration in minutes
            
        Returns:
            Dict with script, titles, description
        """
        return {
            'topic': topic,
            'duration': duration,
            'script': self.generate_script(topic, duration),
            'titles': self.generate_title(topic),
            'description': self.generate_description(topic, duration),
            'thumbnail_brief': self.generate_thumbnail_brief(topic)
        }