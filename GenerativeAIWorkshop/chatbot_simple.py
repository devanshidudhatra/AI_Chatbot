import streamlit as st
import os
import dotenv
import google.generativeai as genai

# Set GOOGLE_APPLICATION_CREDENTIALS environment variable
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/service_account_key.json"

# Load environment variables from .env file
dotenv.load_dotenv()

# Configure gemini API
gemini_api_key = os.getenv("GOOGLE_GEMINI_AI")
genai.configure(api_key=gemini_api_key)

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
