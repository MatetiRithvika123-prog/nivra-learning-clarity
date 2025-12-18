import streamlit as st
import os
from google import genai

# Configure client
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

st.title("Nivra")
st.subheader("Clarity for curious minds")

topic = st.text_input("Enter any topic you're confused about")

if st.button("Get Clarity") and topic:
    try:
        prompt = f"""
Explain the topic "{topic}" clearly for a beginner student.
If it is technical, include:
- a clear definition
- simple explanation
- syntax (if applicable)
- a small example
If it is non-technical, explain in a thoughtful, engaging way.
"""

        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )

        st.success(response.text)

    except Exception as e:
        st.error("Something went wrong.")
        st.exception(e)
