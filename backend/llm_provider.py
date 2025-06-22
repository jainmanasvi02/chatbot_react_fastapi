import os
import httpx
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

async def generate_response(prompt: str) -> str:
    if not GEMINI_API_KEY:
        return "Missing API key."
    
    headers = {
        "Content-Type": "application/json",
    }

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(GEMINI_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()

        # Extracting the response from Gemini
        try:
            return data["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError):
            return "I'm sorry, I couldn't understand that."
