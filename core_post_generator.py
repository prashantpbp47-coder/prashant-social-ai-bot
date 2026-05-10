from core.groq_client import GroqClient
from config.prompts import (
    LINKEDIN_PROMPT, FACEBOOK_PROMPT, 
    INSTAGRAM_PROMPT, TWITTER_PROMPT
)

class PostGenerator:
    def __init__(self):
        """Initialize post generator"""
        self.groq = GroqClient()
        self.prompts = {
            'linkedin': LINKEDIN_PROMPT,
            'facebook': FACEBOOK_PROMPT,
            'instagram': INSTAGRAM_PROMPT,
            'twitter': TWITTER_PROMPT,
        }
    
    def generate_post(self, topic: str, platform: str, 
                     language: str = 'hindi', style: str = 'professional') -> str:
        """
        Generate a social media post
        
        Args:
            topic: Post topic
            platform: Social media platform (linkedin, facebook, etc.)
            language: Language (hindi, english, hinglish)
            style: Writing style
            
        Returns:
            Generated post
        """
        if platform not in self.prompts:
            return f"Platform {platform} not supported"
        
        base_prompt = self.prompts[platform]
        
        # Add language and style instructions
        enhanced_prompt = base_prompt.format(topic=topic)
        
        if language == 'hinglish':
            enhanced_prompt += "\n\nLanguage: Mix of Hindi and English (Hinglish)"
        elif language == 'english':
            enhanced_prompt += "\n\nLanguage: English"
        else:
            enhanced_prompt += "\n\nLanguage: Hindi"
        
        enhanced_prompt += f"\nTone: {style}"
        
        return self.groq.generate_text(enhanced_prompt, temperature=0.7)
    
    def generate_bulk_posts(self, topics: list, platform: str) -> list:
        """
        Generate posts for multiple topics
        
        Args:
            topics: List of topics
            platform: Social media platform
            
        Returns:
            List of generated posts
        """
        posts = []
        for topic in topics:
            post = self.generate_post(topic, platform)
            posts.append({
                'topic': topic,
                'platform': platform,
                'content': post
            })
        return posts
    
    def generate_with_hashtags(self, topic: str, platform: str) -> dict:
        """
        Generate post with suggested hashtags
        
        Args:
            topic: Post topic
            platform: Social media platform
            
        Returns:
            Dict with content and hashtags
        """
        content = self.generate_post(topic, platform)
        
        # Generate hashtags
        hashtag_prompt = f"""
        Topic: {topic}
        Platform: {platform}
        
        Suggest 5-10 relevant hashtags for this topic on {platform}.
        Return as JSON: {{"hashtags": ["#tag1", "#tag2", ...]}}
        """
        
        hashtags_response = self.groq.generate_json(hashtag_prompt)
        
        return {
            'content': content,
            'hashtags': hashtags_response.get('hashtags', []),
            'platform': platform,
            'topic': topic
        }