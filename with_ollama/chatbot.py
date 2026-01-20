import requests
import json

# Configuration
OLLAMA_API_URL = "http://localhost:11434/api/chat" # Using the /api/chat endpoint for multi-turn conversations
MODEL_NAME = "qwen2.5:1.5b" # Make sure this matches the model you pulled

def generate_chat_response(messages):
    """
    Sends a list of messages (conversation history) to the Ollama chat endpoint
    and returns the model's response.
    """
    headers = {"Content-Type": "application/json"}
    data = {
        "model": MODEL_NAME,
        "messages": messages, # List of message objects
        "stream": False # Set to True if you want to stream responses token by token
    }
    try:
        response = requests.post(OLLAMA_API_URL, headers=headers, data=json.dumps(data))
        response.raise_for_status() # Raise an exception for bad status codes

        result = response.json()
        # The /api/chat endpoint returns a 'message' object, not just a 'response' string
        return result.get("message", {}).get("content", "No response content found.")
    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to Ollama. Make sure Ollama is running."
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

def main_cli_chatbot():
    print(f"Chatbot initialized with model: {MODEL_NAME}")
    print("Type 'quit', 'exit', or 'bye' to end the conversation.")

    # Initialize conversation history
    # The Ollama /api/chat endpoint expects a list of messages
    # Each message is a dict with "role" (system, user, assistant) and "content"
    messages = []

    # Optional: Add an initial system message to guide the model
    messages.append({"role": "system", "content": "You are a helpful and concise AI assistant named Qwen-Bot. Keep your answers brief."})

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit","bye"]:
            print("Chatbot: Goodbye!")
            break

        # Add user's message to history
        messages.append({"role": "user", "content": user_input})
        
        # Get response from the model
        response_content = generate_chat_response(messages)
        
        # Add model's response to history
        # Ensure we're adding the content from the model, even if it's an error message
        # For actual model responses, the role will be 'assistant'
        messages.append({"role": "assistant", "content": response_content})

        print(f"Chatbot: {response_content}")

if __name__ == "__main__":
    main_cli_chatbot()