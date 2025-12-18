import streamlit as st
import google.generativeai as genai

# Page config
st.set_page_config(page_title="NIVRA", page_icon="🧠", layout="centered")

st.title("NIVRA")
st.caption("Clarity before confusion.")

# Gemini setup
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-pro")

SYSTEM_PROMPT = """
You are NIVRA — a learning clarity assistant.

Rules:
- Start with a clear definition.
- Explain step-by-step in logical order.
- For technical topics:
  - Provide syntax in the appropriate programming language.
  - Give a small working example.
- For non-technical topics:
  - Explain in a mature, intuitive way.
- Use simple, calm, encouraging language.
- End with a small "next step" suggestion.
"""

topic = st.text_input("Enter any topic you're confused about")

if st.button("Get Clarity") and topic:
    with st.spinner("Bringing clarity..."):
        prompt = f"{SYSTEM_PROMPT}\n\nTopic: {topic}"
        response = model.generate_content(prompt)
        st.markdown(response.text)
