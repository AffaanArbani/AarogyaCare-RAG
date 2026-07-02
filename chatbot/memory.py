"""
Redis memory management for the AarogyaCare RAG chatbot.
"""

import json

from chatbot.config import redis_client


def save_message(session_id: str, role: str, message: str) -> None:
    """
    Save a chat message to Redis.
    """

    key = f"chat:{session_id}"

    data = {
        "role": role,
        "message": message
    }

    redis_client.rpush(
        key,
        json.dumps(data)
    )


def get_chat_history(session_id: str) -> list[dict]:
    """
    Retrieve chat history from Redis.
    """

    key = f"chat:{session_id}"

    messages = redis_client.lrange(
        key,
        0,
        -1
    )

    return [json.loads(msg) for msg in messages]


def clear_chat_history(session_id: str) -> None:
    """
    Delete an entire conversation.
    """

    key = f"chat:{session_id}"

    redis_client.delete(key)