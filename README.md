# 🤖 Kelly – The Local AI Scientist Chatbot

**Kelly** is a local AI chatbot powered by **Ollama** and written in **Python**.  
It is designed to generate poetic yet analytical responses — like a scientist who thinks in verse.  

This version is **not hosted online** because **Ollama models must run locally** and cannot currently be deployed directly on Streamlit Cloud or other free hosting platforms.

---

## ⚙️ Why It Doesn’t Work on Streamlit Cloud

Ollama runs **entire language models locally on your system** (e.g., Mistral, Llama3).  
When Streamlit Cloud tries to run it, it fails because:
1. The server cannot access your local Ollama installation.
2. Ollama models are several gigabytes large and can’t be hosted on free cloud servers.
3. Streamlit’s internal subprocess communication sometimes causes **encoding errors** on Windows (`UnicodeDecodeError`).

Hence, this chatbot must be **run locally** — directly on your own computer.

---

## 🧩 Local Setup Instructions

### 🪄 1. Install Requirements

You need:
- **Python 3.10+**
- **Ollama** (download from [https://ollama.ai/download](https://ollama.ai/download))

### 🧰 2. Clone or Download This Repository
```bash
git clone https://github.com/Jerinjc/Kelly-Chatbot.git
cd Kelly-Chatbot
