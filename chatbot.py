import os
import google.generativeai as genai

API_KEY_PATH = r"C:\Users\ahmtt\Documents\VS\API KEY\BCC_HACKATHON_GEMINI_API_KEY.txt"


def read_api_key(path):
    try:
        with open(path, 'r') as file:
            return file.read().strip()
    except Exception as e:
        print(f"Error reading API key: {e}")
        return None

def gemini_response(api_key, prompt):
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"[Error calling Gemini API: {e}]"

def main():
    api_key = read_api_key(API_KEY_PATH)
    if not api_key:
        print("API key not found. Exiting.")
        return
    print("Chatbot is running. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = gemini_response(api_key, user_input)
        print(f"Gemini: {response}")

if __name__ == "__main__":
    main() 