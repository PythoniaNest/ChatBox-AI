from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

ChatBot_name = 'MyChatBot'
chatbot = ChatBot(ChatBot_name)
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_list = ListTrainer(chatbot)
trainer_corpus.train('chatterbot.corpus.english')
custom_conversations = [
    "Hello",
    "Hi there!",
    "How are you?",
    "I'm doing well, thank you!",
    "What's your name?",
    f"My name is {ChatBot_name}.",
    "Goodbye",
    "See you later!"
]
trainer_list.train(custom_conversations)
def get_response(user_input):
    return chatbot.get_response(user_input)
if __name__ == "__main__":
    print(f"{ChatBot_name} is ready to chat!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print(f"{ChatBot_name}: Goodbye!")
            break
        response = get_response(user_input)
        print(f"{ChatBot_name}: {response}")
