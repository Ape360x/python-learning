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

def ask(prompt, max_tokens=90):
    body = {
        "model": "qwen/qwen3.8-27b",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3,
        "max_tokens": max_tokens,
    }

    try:
        response = requests.post(url, headers=headers, json=body, timeout=30)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Groq request failed: {e}") from e
    else:
        return data["choices"][0]["message"]["content"]


if __name__ == "__main__":
    print(ask("What is a Python dictionary?"))
    print(ask("Give me one tip for beginner weight training."))

    models = requests.get("https://api.groq.com/openai/v1/models", headers=headers, timeout=30).json()
    print([m["id"] for m in models["data"]])