import nltk
import random
from nltk.chat.util import Chat, reflections
import gemi


# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["My name is ChatBot and I'm here to assist you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm doing okay, how about you?",]
    ],
    [
        r"sorry (.*)",
        ["Apologies for any inconvenience.", "No problem, let's move on.",]
    ],
    [
        r"(.*) thank you (.*)",
        ["You're welcome!", "No problem. How can I assist you further?",]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye, have a great day!",]
    ],
]

# Define chatbot
def chatbot():
    print("Hello! I'm ChatBot. How can I assist you today?")

    chat = Chat(pairs, reflections)
    while True:
        user_input = input("You: ")
        response = chat.respond(user_input)
        print("ChatBot:", response)

# Run the chatbot
if __name__ == "__main__":
    chatbot()
