import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model=os.getenv("MODEL_NAME", "llama-3.3-70b-versatile"),
    max_tokens=150,
    temperature=0.7,
)

SYSTEM = SystemMessage(
    content="You are a helpful assistant. Always reply in the same language the user uses. Keep answers short and to the point."
)

# All sessions stored in memory — resets on server restart
sessions: dict = {}


def delete_session(session_id: str) -> None:
    sessions.pop(session_id, None)


def chat(session_id: str, user_message: str) -> str:
    history = sessions.setdefault(session_id, [])
    history.append(HumanMessage(content=user_message))
    # Keep only last 20 messages to stay within token limit
    response = llm.invoke([SYSTEM] + history[-20:])
    reply = response.content
    history.append(AIMessage(content=reply))
    return reply
