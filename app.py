import os
import streamlit as st
from google import genai

st.set_page_config(page_title="Gemini Model Checker")

st.title("Gemini Model Checker")
st.write("This app ONLY lists available models for your API key.")

# Read API key
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    st.error("GEMINI_API_KEY not found in Streamlit Secrets.")
    st.stop()

# Create client
client = genai.Client(api_key=api_key)

st.subheader("Available models:")

try:
    models = client.models.list()
    for model in models:
        st.write(model.name)
except Exception as e:
    st.error("Failed to list models")
    st.exception(e)
