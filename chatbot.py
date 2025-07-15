import os
import requests

SYSTEM_PROMPT = ("You are a helpful assistant. Only answer questions related to finance or college. "
                 "If the question is not about finance or college, politely refuse to answer.\n")

# Read Azure OpenAI configuration from environment variables
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")  # e.g., https://YOUR_RESOURCE_NAME.openai.azure.com/
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")  # e.g., 'gpt-35-turbo' or your deployment name
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2023-05-15")  # Default version


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