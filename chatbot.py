from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from gtts import gTTS
import pygame
import os

def speak(text):
    tts = gTTS(text)
    tts.save("temp.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    os.remove("temp.mp3")


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
    speak(f"{ChatBot_name} is ready to chat!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print(f"{ChatBot_name}: Goodbye!")
            speak("Goodbye!")        
            break
        response = get_response(user_input)
        response_text = str(response)
        print(f"{ChatBot_name}: {response_text}")
        speak(response_text)
