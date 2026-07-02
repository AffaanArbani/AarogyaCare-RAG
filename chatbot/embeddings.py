"""
Embedding helper functions for the AarogyaCare RAG chatbot.
"""

from chatbot.config import embedding_model


def embed_text(text: str) -> list[float]:
    """
    Generate an embedding for a document.
    """
    embedding = embedding_model.encode(
        text,
        convert_to_numpy=True
    )

    return embedding.tolist()


def embed_query(query: str) -> list[float]:
    """
    Generate an embedding for a user query.
    """
    embedding = embedding_model.encode(
        query,
        convert_to_numpy=True
    )

    return embedding.tolist()