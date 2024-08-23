import streamlit as st
import os
import dotenv
import google.generativeai as genai

# Load environment variables from .env file
dotenv.load_dotenv()

# Configure gemini API
gemini_api_key = os.getenv("GOOGLE_GEMINI_AI")
genai.configure(api_key=gemini_api_key)

# Initialize chat history list
chat_history = []

# Define Streamlit UI
st.title("Gemini Chatbot")

# Get user input
prompt = st.text_input("Enter your question:")

# Generate response
if st.button("Generate Response"):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    st.write("Response:")
    st.write(response.text)
    
    # Store chat history
    chat_history.append({"prompt": prompt, "response": response.text})

# Display chat history
if chat_history:
    st.subheader("Chat History:")
    for i, chat in enumerate(chat_history, 1):
        st.write(f"{i}. User: {chat['prompt']}")
        st.write(f"   Chatbot: {chat['response']}")
