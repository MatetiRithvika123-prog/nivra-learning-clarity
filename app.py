import streamlit as st

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Nivra",
    page_icon="🧠",
    layout="centered"
)

st.title("Nivra")
st.caption("Clarity before confusion.")

# -------------------------------
# Helper Logic (Intelligence)
# -------------------------------
TECH_KEYWORDS = [
    "programming", "code", "class", "object", "loop", "variable",
    "algorithm", "data", "network", "python", "java", "c++", "db",
    "function", "method", "array", "stack", "queue"
]

def is_technical(topic: str) -> bool:
    topic = topic.lower()
    return any(word in topic for word in TECH_KEYWORDS)

def generate_clarity(topic: str) -> str:
    if is_technical(topic):
        return f"""
### 📘 Topic: {topic}

#### **Definition**
{topic.capitalize()} is a concept used in computer science to help programs stay flexible, reusable, and easier to understand as they grow.

#### **Step-by-step explanation**
1. It exists to avoid repeating similar logic.
2. It allows the same idea to behave differently based on context.
3. This makes programs easier to extend and maintain.
4. Misunderstanding it often leads to rigid or confusing code.

#### **Basic syntax (example in Python)**

```python
class Example:
    def action(self):
        print("Doing something")
