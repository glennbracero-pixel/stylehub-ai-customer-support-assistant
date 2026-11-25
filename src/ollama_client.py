import requests


OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "qwen3.5:4b"


def ask_ollama(prompt):
    """Send a prompt to Ollama and return the AI response."""

    payload = {
    "model": MODEL_NAME,
    "messages": [{"role": "user", "content": prompt}],
    "stream": False,
    "think": False,
    "options": {
        "num_ctx": 4096,
        "num_predict": 256,
        "temperature": 0.2
    }
}

    try:
        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=600
        )

        response.raise_for_status()

        result = response.json()

        return result["message"]["content"]

    except requests.exceptions.RequestException as error:
        print(f"Could not communicate with Ollama: {error}")
        return None


if __name__ == "__main__":

    print("Testing connection to Qwen...")

    answer = ask_ollama(
        "Reply with exactly: StyleHub AI connection successful!"
    )

    if answer:
        print("\nAI response:")
        print(answer)
    else:
        print("\nAI connection test failed.")