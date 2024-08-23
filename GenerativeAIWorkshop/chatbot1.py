import streamlit as st

# Define pairs of patterns and responses
pairs = {
    "hi": "Hello!",
    "how are you?": "I'm doing well, thank you!",
    "what is your name?": "I'm a chatbot. What's yours?",
    "bye": "Goodbye! Have a great day!"
}

# Define chatbot function
def chatbot(user_input):
    response = pairs.get(user_input.lower(), "I'm sorry, I don't understand that.")
    return response

# Streamlit interface
st.title("Simple Chatbot")

user_input = st.text_input("You: ", "")
if st.button("Send"):
    response = chatbot(user_input)
    st.text_area("Chatbot:", value=response, height=100)

