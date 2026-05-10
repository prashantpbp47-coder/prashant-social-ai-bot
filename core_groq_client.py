import groq
from config.settings import GROQ_API_KEY, GROQ_MODEL, MAX_TOKENS
import json

class GroqClient:
    def __init__(self):
        """Initialize Groq client"""
        self.client = groq.Groq(api_key=GROQ_API_KEY)
        self.model = GROQ_MODEL
        
    def generate_text(self, prompt: str, temperature: float = 0.7) -> str:
        """
        Generate text using Groq API
        
        Args:
            prompt: The prompt for AI
            temperature: Creativity level (0-1)
            
        Returns:
            Generated text
        """
        try:
            message = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=temperature,
                max_tokens=MAX_TOKENS,
            )
            return message.choices[0].message.content
        
        except Exception as e:
            return f"Error generating text: {str(e)}"
    
    def generate_json(self, prompt: str) -> dict:
        """
        Generate JSON response from Groq
        
        Args:
            prompt: The prompt asking for JSON
            
        Returns:
            Parsed JSON response
        """
        try:
            response = self.generate_text(prompt)
            # Extract JSON from response
            start = response.find('{')
            end = response.rfind('}') + 1
            if start != -1 and end > start:
                json_str = response[start:end]
                return json.loads(json_str)
            return {"error": "Could not parse JSON"}
        except Exception as e:
            return {"error": str(e)}
    
    def batch_generate(self, prompts: list) -> list:
        """
        Generate text for multiple prompts
        
        Args:
            prompts: List of prompts
            
        Returns:
            List of generated texts
        """
        results = []
        for prompt in prompts:
            result = self.generate_text(prompt)
            results.append(result)
        return results