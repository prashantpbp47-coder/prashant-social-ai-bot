# 🚀 Prashant Social AI Bot

**AI-powered social media & YouTube content creator** for automating your digital marketing!

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.8+-blue)

---

## 🎯 Features

### 📱 Multi-Platform Support
- ✅ LinkedIn
- ✅ Facebook
- ✅ Instagram
- ✅ Twitter/X
- ✅ YouTube (coming soon)

### 🎬 YouTube Content Creation
- 📜 AI Script Generation
- 🎯 Title & Description Generation
- 🎨 Thumbnail Design
- 📝 Auto Subtitle Generation
- 📊 Video Analytics
- 📅 Schedule Publishing

### 💡 AI-Powered Features
- Groq LLaMA 3 API integration
- Hindi + English + Hinglish support
- Multiple writing styles
- SEO-optimized content
- Bulk post generation

### 🔧 Production Ready
- REST API with Flask
- Docker support
- CI/CD pipeline
- Error handling & logging
- Environment configuration

---

## 📋 Prerequisites

- Python 3.8+
- Groq API Key ([get free](https://console.groq.com))
- YouTube API Key (optional, for YouTube features)
- Docker (optional, for containerized deployment)

---

## 🚀 Quick Start

### 1️⃣ Clone Repository
\`\`\`bash
git clone https://github.com/prashantpbp47-coder/prashant-social-ai-bot.git
cd prashant-social-ai-bot
\`\`\`

### 2️⃣ Run Setup
\`\`\`bash
chmod +x setup.sh
./setup.sh
\`\`\`

### 3️⃣ Configure Environment
\`\`\`bash
# Edit .env file
nano .env

# Add your API keys:
GROQ_API_KEY=your_key_here
YOUTUBE_API_KEY=your_key_here (optional)
\`\`\`

### 4️⃣ Run Quick Demo
\`\`\`bash
source venv/bin/activate
python quick_start.py
\`\`\`

### 5️⃣ Start API Server
\`\`\`bash
python api/app.py