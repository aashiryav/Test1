import os

API_KEY_PATH = r"C:\Users\ahmtt\Documents\VS\API KEY\BCC_HACKATHON_GEMINI_API_KEY.txt"

def read_api_key(path):
    try:
        with open(path, 'r') as file:
            return file.read().strip()
    except Exception as e:
        print(f"Error reading API key: {e}")
        return None

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
        # Placeholder for API call using api_key and user_input
        print(f"[Simulated response to '{user_input}']")

if __name__ == "__main__":
    main() 