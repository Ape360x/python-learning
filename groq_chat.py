import os
import requests
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("GROQ_API_KEY")

url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json",
}

def ask(prompt):
    body = {
        "model": "allam-2-7b",
        "messages": [
            {"role": "user", "content": prompt}
        ],
    }

    try:
        response = requests.post(url, headers=headers, json=body, timeout=30)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.HTTPError as e:
        print("Groq returned an error:", e)
        print(response.text)          # ← the real reason is in here
    else:
        return data["choices"][0]["message"]["content"]


print(ask("What is a Python dictionary?"))
print(ask("Give me one tip for beginner weight training."))


models = requests.get("https://api.groq.com/openai/v1/models", headers=headers, timeout=30).json()
print([m["id"] for m in models["data"]])