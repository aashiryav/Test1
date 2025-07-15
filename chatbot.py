import os
import requests
import sys

SYSTEM_PROMPT = ("You are a helpful assistant. Only answer questions related to finance or college. "
                 "If the question is not about finance or college, politely refuse to answer.\n")

SECRET_PATH = r"C:\Users\ahmtt\Documents\VS\API KEY"
if SECRET_PATH not in sys.path:
    sys.path.insert(0, SECRET_PATH)
try:
    from secret import AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_DEPLOYMENT, AZURE_OPENAI_API_KEY
except ImportError:
    AZURE_OPENAI_ENDPOINT = None
    AZURE_OPENAI_DEPLOYMENT = None
    AZURE_OPENAI_API_KEY = None

AZURE_OPENAI_API_VERSION = "2023-05-15"  # Default version


def azure_openai_response(prompt):
    if not (AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY and AZURE_OPENAI_DEPLOYMENT):
        return "[Azure OpenAI configuration is missing. Please set the required environment variables.]"
    url = f"{AZURE_OPENAI_ENDPOINT}openai/deployments/{AZURE_OPENAI_DEPLOYMENT}/chat/completions?api-version={AZURE_OPENAI_API_VERSION}"
    headers = {
        "Content-Type": "application/json",
        "api-key": AZURE_OPENAI_API_KEY
    }
    data = {
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 512,
        "temperature": 0.7
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"[Error calling Azure OpenAI API: {e}]"


def main():
    print("Chatbot is running. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = azure_openai_response(user_input)
        print(f"Azure: {response}")

if __name__ == "__main__":
    main() 