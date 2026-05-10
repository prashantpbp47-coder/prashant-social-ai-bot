#!/usr/bin/env python3
"""
Quick start demo for Prashant Social AI Bot
Run this to test all features
"""

import os
from dotenv import load_dotenv
from core.post_generator import PostGenerator
from core.video_generator import VideoGenerator
from core.video_editor import VideoEditor

# Load environment variables
load_dotenv()

def print_header(text):
    """Print formatted header"""
    print("\n" + "="*70)
    print(f"  {text}")
    print("="*70 + "\n")

def demo_social_posts():
    """Demo: Generate social media posts"""
    print_header("📱 SOCIAL MEDIA POST GENERATION")
    
    post_gen = PostGenerator()
    
    topics = [
        "AI से इंश्योरेंस मार्केटिंग कैसे करें",
        "PB Partners एजेंट बनने के 5 फायदे",
        "AR फिल्टर से बिजनेस कैसे बढ़ाएं"
    ]
    
    platforms = ['linkedin', 'facebook', 'instagram']
    
    for topic in topics:
        print(f"\n📝 Topic: {topic}")
        print("-" * 70)
        
        for platform in platforms:
            post = post_gen.generate_post(topic, platform, language='hindi')
            print(f"\n{platform.upper()}:\n{post}\n")

def demo_youtube_content():
    """Demo: Generate YouTube content"""
    print_header("🎬 YOUTUBE CONTENT GENERATION")
    
    video_gen = VideoGenerator()
    
    topic = "AI से YouTuber कैसे बनें"
    duration = 5
    style = "educational"
    
    print(f"Topic: {topic}")
    print(f"Duration: {duration} minutes")
    print(f"Style: {style}\n")
    
    # Generate script
    print("\n📜 SCRIPT:")
    print("-" * 70)
    script = video_gen.generate_script(topic, duration, style)
    print(script)
    
    # Generate titles
    print("\n\n🎯 SUGGESTED TITLES:")
    print("-" * 70)
    titles = video_gen.generate_title(topic)
    for i, title in enumerate(titles, 1):
        print(f"{i}. {title}")
    
    # Generate description
    print("\n\n📋 DESCRIPTION:")
    print("-" * 70)
    description = video_gen.generate_description(topic, duration)
    print(description)
    
    # Generate thumbnail brief
    print("\n\n🎨 THUMBNAIL BRIEF:")
    print("-" * 70)
    brief = video_gen.generate_thumbnail_brief(topic, color='red', text='AI')
    print(brief)

def demo_video_editing():
    """Demo: Video editing features"""
    print_header("🎥 VIDEO EDITING FEATURES")
    
    video_editor = VideoEditor()
    
    # Generate thumbnail
    print("\n1️⃣ Generating Thumbnail...")
    thumbnail_path = video_editor.generate_thumbnail(
        title="AI से कमाई करें",
        subtitle="Complete Guide 2026",
        color=(255, 0, 0)
    )
    print(f"✅ Thumbnail saved: {thumbnail_path}")
    
    # Generate subtitles
    print("\n2️⃣ Generating Subtitles...")
    script = "आज हम सीखेंगे कि AI से कैसे पैसा कमाया जाता है। यह बहुत आसान है।"
    subtitle_path = video_editor.generate_subtitle_file(script)
    print(f"✅ Subtitles saved: {subtitle_path}")

def demo_full_package():
    """Demo: Complete video package"""
    print_header("📦 COMPLETE VIDEO PACKAGE")
    
    video_gen = VideoGenerator()
    topic = "Social Media Automation से कमाई"
    
    package = video_gen.generate_full_video_package(topic, duration=5)
    
    print(f"\nTopic: {package['topic']}")
    print(f"Duration: {package['duration']} minutes\n")
    
    print("SCRIPT:")
    print("-" * 70)
    print(package['script'][:500] + "...\n")
    
    print("\nTITLES:")
    for i, title in enumerate(package['titles'], 1):
        print(f"  {i}. {title}")
    
    print("\n\nDESCRIPTION:")
    print("-" * 70)
    print(package['description'][:300] + "...\n")

def main():
    """Run all demos"""
    print("\n")
    print("╔" + "="*68 + "╗")
    print("║" + " "*15 + "🚀 PRASHANT SOCIAL AI BOT - QUICK START" + " "*14 + "║")
    print("╚" + "="*68 + "╝")
    
    try:
        # Check API key
        if not os.getenv('GROQ_API_KEY'):
            print("\n❌ ERROR: GROQ_API_KEY not found in .env file")
            print("Please set GROQ_API_KEY in your .env file")
            return
        
        print("\n✅ API Key found!")
        print("\n📋 Demo Options:")
        print("  1. Social Media Posts")
        print("  2. YouTube Content")
        print("  3. Video Editing")
        print("  4. Full Package (All Together)")
        print("  5. Run All Demos")
        
        # For automated demo, run all
        demo_social_posts()
        demo_youtube_content()
        demo_video_editing()
        demo_full_package()
        
        print_header("✅ DEMO COMPLETED SUCCESSFULLY!")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()