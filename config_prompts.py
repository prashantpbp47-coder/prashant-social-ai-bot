# Social Media Prompts
LINKEDIN_PROMPT = """
तुम Prashant हो - PB Partners के AI Expert।

एक professional LinkedIn post लिखो हिंदी में:

Topic: {topic}

Rules:
- 100-150 शब्द
- Professional लेकिन friendly tone
- #PrashantAI #PBPartners hashtags लगाओ
- Call-to-action जरूर दो
- Data/facts use करो अगर relevant हो
"""

FACEBOOK_PROMPT = """
एक engaging Facebook post लिखो:

Topic: {topic}

Rules:
- 150-200 शब्द
- Casual & friendly tone
- Emojis use करो
- Story-telling style
- लोगों को engage करने के लिए सवाल पूछो
- #PBPartners हैशटैग लगाओ
"""

INSTAGRAM_PROMPT = """
एक Instagram caption लिखो:

Topic: {topic}

Rules:
- 50-100 शब्द
- Trendy & catchy
- Lots of emojis 😊
- Hashtags (10-15)
- CTA (Call To Action) include करो
- Hook से शुरू करो
"""

TWITTER_PROMPT = """
एक Twitter/X thread लिखो (3-5 tweets):

Topic: {topic}

Rules:
- हर tweet 280 characters में
- Numbered (1/, 2/, etc.)
- Interesting facts/insights
- Conversational tone
- Hashtags use करो
- Call-to-action last tweet में
"""

# YouTube Prompts
YOUTUBE_SCRIPT_PROMPT = """
एक {duration} मिनट की YouTube video के लिए script लिखो।

Topic: {topic}
Style: {style}
Language: {language}

Structure:
[HOOK - 15 seconds]
एक attention-grabbing opening जो लोगों को रोके।

[INTRO - 30 seconds]
अपना नाम, channel introduction, topic overview।

[MAIN CONTENT - {main_duration} seconds]
Detailed explanation, examples, tips।

[CTA - 15 seconds]
Subscribe करने के लिए कहो, next video के लिए teaser दो।

[OUTRO - 15 seconds]
"Thanks for watching! See you next time!"

Requirements:
- हिंदी में clear, simple language
- Technical जानकारी को simple बनाओ
- Real-life examples दो
- Engaging रखो
- Timestamp-friendly हो
"""

YOUTUBE_TITLE_PROMPT = """
एक catchy YouTube video title suggest करो:

Topic: {topic}

Rules:
- 50-60 characters में
- SEO-friendly
- CTR (Click-Through-Rate) बढ़ाने वाला
- Numbers/emojis use कर सकते हो
- "{topic} | ..." format में

3-5 options दो।
"""

YOUTUBE_DESCRIPTION_PROMPT = """
एक YouTube video description लिखो:

Topic: {topic}
Video Duration: {duration} minutes

Requirements:
- पहली line में सबसे important info (250 characters)
- Timestamps के साथ chapters
- Related links/resources
- Social media links
- Subscribe CTA
- 2-3 relevant hashtags
- 300-500 words

Format:
[Hook/Summary]
[Chapters with timestamps]
[Resources/Links]
[Social Links]
[Hashtags]
"""

THUMBNAIL_PROMPT = """
एक YouTube thumbnail के लिए design brief दो:

Topic: {topic}
Main Color: {color}
Text: {text}

Design Tips:
- Bold, readable text
- High contrast
- Face expression (if applicable)
- Minimal text (4-5 words max)
- Professional look
"""