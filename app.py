import os
import streamlit as st
from google import genai

# Page setup
st.set_page_config(
    page_title="Nivra",
    page_icon="🧠",
    layout="centered"
)

st.title("Nivra")
st.caption("Clarity before confusion.")

# Read API key from Streamlit Secrets
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    st.error("GEMINI_API_KEY not found in Secrets.")
    st.stop()

# Create Gemini client
client = genai.Client(api_key=api_key)

topic = st.text_input(
    "Enter any topic you're stuck with",
    placeholder="e.g. Explain loops in Python"
)

if st.button("Get Clarity") and topic.strip():
    with st.spinner("Bringing clarity..."):
        try:
            prompt = f"""
You are Nivra, a learning clarity assistant.

Rules:
- Start with a clear definition.
- Explain step by step in simple, structured language.
- If the topic is technical, include syntax and a small example.
- If non-technical, explain in a mature, intuitive way.
- End with a small next-step suggestion.

Topic:
{topic}
"""
            response = client.models.generate_content(
                model="models/gemini-2.0-flash",
                contents=prompt
            )

            st.markdown(response.text)

        except Exception as e:
            st.error("Something went wrong.")
            st.exception(e)
