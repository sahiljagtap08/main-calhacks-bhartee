import os
import requests
from groq import Groq

# Initialize Groq client
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Perplexity AI API endpoint
PERPLEXITY_API_URL = "https://api.perplexity.ai/chat/completions"
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")

def generate_groq_response(prompt: str, max_tokens: int = 1000):
    try:
        response = groq_client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama2-70b-4096",  # or another suitable Groq model
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating Groq response: {e}")
        return None

def generate_perplexity_response(prompt: str):
    headers = {
        "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mixtral-8x7b-instruct",
        "messages": [{"role": "user", "content": prompt}]
    }
    try:
        response = requests.post(PERPLEXITY_API_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error generating Perplexity response: {e}")
        return None

def generate_combined_response(prompt: str):
    groq_response = generate_groq_response(prompt)
    perplexity_response = generate_perplexity_response(prompt)
    
    combined_response = f"Groq Response:\n{groq_response}\n\nPerplexity Response:\n{perplexity_response}"
    return combined_response

