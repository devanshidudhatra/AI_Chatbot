from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter

# Define a custom logic adapter to handle greetings and farewells
class CustomAdapter(LogicAdapter):
    def can_process(self, statement):
        text = statement.text.lower()
        return 'hello' in text or 'hi' in text or 'bye' in text or 'goodbye' in text

    def process(self, statement, additional_response_selection_parameters):
        import random
        from chatterbot.conversation import Statement

        text = statement.text.lower()
        if 'hello' in text or 'hi' in text:
            response_text = random.choice(['Hello!', 'Hi there!', 'Greetings!'])
        elif 'bye' in text or 'goodbye' in text:
            response_text = random.choice(['Goodbye!', 'Bye!', 'See you later!'])
        else:
            response_text = 'I am not sure how to respond to that.'

        response_statement = Statement(text=response_text)
        response_statement.confidence = 1
        return response_statement

# Create the chatbot
chatbot = ChatBot(
    'BasicBot',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        {'import_path': 'chatterbot.logic.BestMatch'},
        {'import_path': 'CustomAdapter'}
    ],
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

# Train the chatbot with some basic responses
trainer = ListTrainer(chatbot)
trainer.train([
    "How are you?",
    "I am good, thank you!",
    "What is your name?",
    "I am BasicBot, your friendly chatbot.",
    "What can you do?",
    "I can chat with you and remember our conversations.",
    "Tell me a joke.",
    "Why don't scientists trust atoms? Because they make up everything!",
    "What is the capital of France?",
    "The capital of France is Paris."
])

# Function to handle conversation with memory
def get_response_with_memory(chatbot, user_input, chat_memory):
    response = chatbot.get_response(user_input)
    chat_memory.append((user_input, response.text))
    return response

# Main chat flow
def chat_with_bot():
    chat_memory = []
    print("BasicBot: Hello! How can I help you today?")
    
    # Chatbot asks questions
    questions = ["What is your name?", "How old are you?", "What is your favorite color?"]
    for question in questions:
        print("BasicBot:", question)
        user_response = input("You: ")
        get_response_with_memory(chatbot, user_response, chat_memory)
    
    # Main conversation loop
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "goodbye"]:
            print("BasicBot: Goodbye!")
            break
        response = get_response_with_memory(chatbot, user_input, chat_memory)
        print("BasicBot:", response)

        # Error handling
        if response.confidence < 0.5:
            print("BasicBot: I'm sorry, I didn't understand that. Can you please rephrase?")

# Run the chat
chat_with_bot()
