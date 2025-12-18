import streamlit as st

st.set_page_config(
    page_title="NIVRA",
    page_icon="🧠",
    layout="centered"
)

st.title("NIVRA")
st.caption("Clarity for curious minds.")

topic = st.text_input(
    "What topic are you confused about?",
    placeholder="e.g. loops in Python"
)

def generate_nivra_explanation(topic: str) -> str:
    return f"""
### 📘 Topic: {topic}

**Definition**  
{topic} is explained here in a clear and beginner-friendly way, focusing on what it means and why it exists.

**Step-by-step explanation**
1. What the concept is meant to do  
2. How it works internally  
3. When and why it is used  
4. What happens if it is misunderstood  

**If this is a technical topic**
- Show the basic syntax
- Explain each part of the syntax
- Provide a simple example

**If this is a non-technical topic**
- Explain using an intuitive, real-world analogy
- Avoid jargon
- Focus on understanding rather than memorization

**Common mistakes**
- Misunderstanding the purpose
- Skipping foundational ideas
- Jumping ahead too quickly

**Next step**
Search for one simple example related to **{topic}** and try to explain it in your own words.
"""

if st.button("Get Clarity") and topic.strip():
    explanation = generate_nivra_explanation(topic)
    st.markdown(explanation)
