from google import genai
import os

api_key = os.environ.get("GOOGLE_API_KEY") or "AIzaSyC0ueP_aIuPucZGfITgLKwT-n1VdnBxcU0"
client = genai.Client(api_key=api_key)

for m in client.models.list():
    print(m.name)
