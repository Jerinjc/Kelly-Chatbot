import streamlit as st
import subprocess
import textwrap

# -------------------------------
# 🎨 Streamlit Page Config
# -------------------------------
st.set_page_config(
    page_title="Kelly - The AI Scientist Poet",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# -------------------------------
# 🧵 Custom Styling
# -------------------------------
st.markdown("""
    <style>
    body {
        background-color: #f7f8fc;
    }
    .main {
        background-color: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    }
    .title {
        font-family: 'Georgia', serif;
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        color: #2C3E50;
        margin-bottom: -0.5rem;
    }
    .subtitle {
        text-align: center;
        color: #7F8C8D;
        margin-bottom: 2rem;
    }
    .chat-bubble-user {
        background-color: #d7eaf3;
        color: #2C3E50;
        padding: 0.8rem 1rem;
        border-radius: 12px;
        margin-bottom: 0.8rem;
        text-align: right;
    }
    .chat-bubble-bot {
        background-color: #f0f0f0;
        color: #2C3E50;
        padding: 1rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        font-style: italic;
        border-left: 4px solid #2C3E50;
    }
    .footer {
        text-align: center;
        font-size: 0.9rem;
        color: #95A5A6;
        margin-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)


# -------------------------------
# 🧠 Helper: Call Ollama Locally
# -------------------------------
def call_ollama(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", "mistral"],
            input=prompt.encode('utf-8'),
            capture_output=True,
            check=True
        )
        # decode safely as utf-8 to avoid Windows cp1252 issue
        return result.stdout.decode('utf-8', errors='ignore').strip()
    except subprocess.CalledProcessError as e:
        return f"❌ Ollama Error:\n{e.stderr}"


# -------------------------------
# 💬 Streamlit App Layout
# -------------------------------
st.markdown("<div class='title'>Kelly 🧠</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>The Skeptical AI Scientist Poet</div>", unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat UI
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.markdown(f"<div class='chat-bubble-user'>{chat['content']}</div>", unsafe_allow_html=True)
    else:
        formatted_text = "<br>".join(textwrap.fill(line, 80) for line in chat["content"].split("\n"))
        st.markdown(f"<div class='chat-bubble-bot'>{formatted_text}</div>", unsafe_allow_html=True)

# Chat input box
user_input = st.chat_input("Ask Kelly something about AI or science...")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Build poetic prompt
    prompt = f"""
    You are Kelly, the AI Scientist Poet.
    Respond in a skeptical, analytical, and professional poetic tone.
    Question: {user_input}

    Your poem must:
    - Question broad claims about AI
    - Highlight possible limitations or biases
    - End with a practical, evidence-based suggestion
    - Be about 8–12 lines long
    """

    # Generate and append response
    response = call_ollama(prompt)
    st.session_state.chat_history.append({"role": "assistant", "content": response})
    st.rerun()

# Footer
st.markdown("<div class='footer'>Powered by Ollama + Mistral</div>", unsafe_allow_html=True)
