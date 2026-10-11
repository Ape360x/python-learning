import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("GROQ_API_KEY")

if key:
    print("key loaded. Length", len(key), "starts with gsk_:", key.startswith("gsk_"))
else:
    print("No key founded. Is the .env file in the right folder?")