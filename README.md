# 🤖 MemoryBot — Chatbot

A chatbot that remembers previous messages and responds contextually using LangChain + Groq + Streamlit.

## Features
- Context-aware responses
- Remembers last 10 conversations per session
- Multiple independent user sessions

## Tech Stack
- **Streamlit** — Chat UI
- **LangChain** — LLM framework
- **Groq (LLaMA 3.3 70B)** — LLM model

## Setup

1. Install dependencies
```bash
pip install -r requirements.txt
```

2. Create `.env` file
```
GROQ_API_KEY=your_api_key_here
MODEL_NAME=llama-3.3-70b-versatile
```

3. Run the app
```bash
streamlit run streamlit_app.py
```

## How Memory Works
Every message is stored in a session-specific history list. The last 20 messages are passed to the LLM as context, allowing the bot to remember previous conversations.

Each session has a unique ID, so multiple users can chat independently.
