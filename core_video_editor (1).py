import os
import cv2
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
from config.settings import VIDEO_OUTPUT_DIR, THUMBNAIL_SIZE

class VideoEditor:
    def __init__(self):
        """Initialize video editor"""
        self.output_dir = VIDEO_OUTPUT_DIR
        os.makedirs(self.output_dir, exist_ok=True)
    
    def generate_thumbnail(self, title: str, subtitle: str = '', 
                          color: tuple = (255, 0, 0), 
                          output_path: str = None) -> str:
        """
        Generate YouTube thumbnail
        
        Args:
            title: Main title text
            subtitle: Subtitle text
            color: RGB color tuple
            output_path: Path to save thumbnail
            
        Returns:
            Path to generated thumbnail
        """
        if output_path is None:
            output_path = os.path.join(self.output_dir, 'thumbnail.png')
        
        # Create image
        img = Image.new('RGB', THUMBNAIL_SIZE, color=color)
        draw = ImageDraw.Draw(img)
        
        # Add text (using default font)
        title_size = 80
        subtitle_size = 40
        
        # Title
        title_bbox = draw.textbbox((0, 0), title)
        title_width = title_bbox[2] - title_bbox[0]
        title_x = (THUMBNAIL_SIZE[0] - title_width) // 2
        draw.text((title_x, 200), title, fill=(255, 255, 255))
        
        # Subtitle
        if subtitle:
            subtitle_bbox = draw.textbbox((0, 0), subtitle)
            subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
            subtitle_x = (THUMBNAIL_SIZE[0] - subtitle_width) // 2
            draw.text((subtitle_x, 400), subtitle, fill=(255, 255, 255))
        
        img.save(output_path)
        return output_path
    
    def add_text_overlay(self, video_path: str, text: str, 
                        position: tuple = (50, 50),
                        duration: int = None) -> str:
        """
        Add text overlay to video
        
        Args:
            video_path: Path to input video
            text: Text to overlay
            position: (x, y) position
            duration: Duration to show text (seconds)
            
        Returns:
            Path to output video
        """
        output_path = os.path.join(self.output_dir, 'video_with_text.mp4')
        
        # Basic implementation - can be enhanced with moviepy
        # For now, just return the path
        return output_path
    
    def create_slideshow(self, images: list, duration_per_image: int = 3,
                        output_path: str = None) -> str:
        """
        Create video from images
        
        Args:
            images: List of image paths
            duration_per_image: Duration to show each image (seconds)
            output_path: Path to save video
            
        Returns:
            Path to generated video
        """
        if output_path is None:
            output_path = os.path.join(self.output_dir, 'slideshow.mp4')
        
        # Implementation using OpenCV
        if not images:
            return None
        
        # Get image dimensions
        first_image = cv2.imread(images[0])
        height, width = first_image.shape[:2]
        
        # Video writer
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        fps = 1 / duration_per_image
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
        
        # Add each image
        for image_path in images:
            img = cv2.imread(image_path)
            if img is not None:
                # Repeat each image for duration
                for _ in range(int(duration_per_image * fps)):
                    out.write(img)
        
        out.release()
        return output_path
    
    def generate_subtitle_file(self, script: str, output_path: str = None) -> str:
        """
        Generate SRT subtitle file from script
        
        Args:
            script: Video script
            output_path: Path to save SRT file
            
        Returns:
            Path to generated SRT file
        """
        if output_path is None:
            output_path = os.path.join(self.output_dir, 'subtitles.srt')
        
        # Simple implementation - splits by sentences
        sentences = script.split('.')
        srt_content = ""
        
        start_time = 0
        for idx, sentence in enumerate(sentences, 1):
            sentence = sentence.strip()
            if not sentence:
                continue
            
            # Estimate duration: ~5 characters per second
            duration = max(1, len(sentence) // 5)
            end_time = start_time + duration
            
            srt_content += f"{idx}\n"
            srt_content += f"{self._format_time(start_time)} --> {self._format_time(end_time)}\n"
            srt_content += f"{sentence}\n\n"
            
            start_time = end_time
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(srt_content)
        
        return output_path
    
    @staticmethod
    def _format_time(seconds: int) -> str:
        """Format seconds to SRT time format (HH:MM:SS,mmm)"""
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60
        return f"{hours:02d}:{minutes:02d}:{secs:02d},000"