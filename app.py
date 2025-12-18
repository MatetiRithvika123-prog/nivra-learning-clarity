import streamlit as st
import google.generativeai as genai
import os

# Page config
st.set_page_config(
    page_title="Nivra — Learning Clarity",
    page_icon="🧠",
    layout="centered"
)

st.title("Nivra")
st.subheader("Clarity for curious minds")

# Load API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("Gemini API key not found. Please add it in Secrets.")
    st.stop()

genai.configure(api_key=api_key)

# IMPORTANT: correct model name
model = genai.GenerativeModel("models/gemini-1.0-pro")



# UI
topic = st.text_input(
    "Enter any topic you're confused about",
    placeholder="e.g. What is computer networks?"
)

if st.button("Get Clarity"):
    if not topic.strip():
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Thinking clearly..."):
            try:
                prompt = f"""
Explain the following topic clearly and step by step.

Rules:
- Start with a clear definition
- Use simple but correct technical language
- If technical, include syntax and example
- End with curiosity-driven next step

Topic:
{topic}
"""
                response = model.generate_content(prompt)
                st.success("Here’s the clarity:")
                st.write(response.text)

            except Exception as e:
                st.error("Something went wrong.")
                st.exception(e)
