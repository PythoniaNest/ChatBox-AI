# ChatBox-AI 🤖

An intelligent chatbot built with Python using ChatterBot, spaCy, and machine learning techniques for natural language processing.

## Features ✨

- **Natural Language Processing**: Powered by spaCy for advanced NLP capabilities
- **Intelligent Responses**: Uses machine learning to generate contextual responses
- **Easy Training**: Train the bot with custom conversations and corpus data
- **Interactive Chat**: Real-time conversation with user-friendly interface
- **Extensible Architecture**: Easy to add new training data and customize responses

## Quick Start 🚀

### Prerequisites

- Python 3.12+
- Virtual Environment (recommended)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/PythoniaNest/ChatBox-AI.git
cd ChatBox-AI
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install chatterbot chatterbot-corpus pyyaml
python -m spacy download en_core_web_sm
```

### Running the Chatbot

```bash
python chatbot.py
```

Start chatting! Type `bye`, `exit`, or `quit` to end the conversation.

## Project Structure 📁

```
ChatBox-AI/
├── chatbot.py           # Main chatbot script
├── db.sqlite3          # Chat history database
├── .venv/              # Virtual environment
└── README.md           # This file
```

## How It Works 🧠

The chatbot uses:
- **ChatterBot**: For conversation training and response generation
- **spaCy**: For natural language understanding and processing
- **SQLite**: For persistent conversation storage
- **Corpus Training**: Pre-trained conversations for better responses
- **Custom Training**: User-defined conversations for personalized behavior

## Dependencies 📦

- `chatterbot` - Core chatbot engine
- `chatterbot-corpus` - Training data and conversation corpus
- `pyyaml` - YAML file parsing for corpus data
- `spacy` - Advanced NLP and language model
- `SQLAlchemy` - ORM for database operations

## Usage Example 💬

```python
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create chatbot instance
chatbot = ChatBot('MyChatBot')

# Train with custom conversations
trainer = ListTrainer(chatbot)
trainer.train([
    "Hello",
    "Hi there!",
    "How are you?",
    "I'm doing well!"
])

# Get responses
response = chatbot.get_response("Hello")
print(response)  # Output: Hi there!
```

## Contributing 🤝

Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License 📜

This project is open source and available under the MIT License.

## Author 👨‍💻

Created by PythoniaNest Team

---

**Happy Chatting!** 💬✨


to start : /mnt/ad6ce59d-1334-41ec-be0b-0e1a3d7064c7/Program/AI/Chatterbox02/.venv/bin/python chatbot.py