"""
FastAPI backend for the AarogyaCare RAG chatbot.
"""

import uuid

from fastapi import FastAPI
from pydantic import BaseModel

from chatbot.rag import chat
from chatbot.memory import clear_chat_history


# =====================================================
# FastAPI App
# =====================================================

app = FastAPI(
    title="AarogyaCare API",
    description="Healthcare RAG Chatbot API",
    version="1.0.0",
)


# =====================================================
# Request Models
# =====================================================

class ChatRequest(BaseModel):
    session_id: str
    message: str


class ChatResponse(BaseModel):
    response: str


# =====================================================
# Routes
# =====================================================

@app.get("/")
def home():

    return {
        "status": "running",
        "message": "AarogyaCare API is running."
    }


@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):

    answer = chat(
        session_id=request.session_id,
        question=request.message,
    )

    return ChatResponse(response=answer)


@app.delete("/chat/{session_id}")
def clear_session(session_id: str):

    clear_chat_history(session_id)

    return {
        "message": "Conversation cleared successfully."
    }


@app.get("/session")
def create_session():

    return {
        "session_id": str(uuid.uuid4())
    }