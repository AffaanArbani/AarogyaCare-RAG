"""
Retriever module for the AarogyaCare RAG chatbot.

This module searches Pinecone for the most
relevant medical documents.
"""

from chatbot.config import pinecone_index
from chatbot.embeddings import embed_query


def retrieve_context(query: str, top_k: int = 3) -> list[dict]:
    """
    Retrieve the most relevant documents.

    Args:
        query (str): User question
        top_k (int): Number of documents to retrieve

    Returns:
        list[dict]: Retrieved documents
    """

    query_embedding = embed_query(query)

    response = pinecone_index.query(
        vector=query_embedding,
        top_k=top_k,
        include_metadata=True
    )

    documents = []

    for match in response["matches"]:

        documents.append(
            {
                "disease": match["metadata"]["disease"],
                "text": match["metadata"]["text"],
                "score": float(match["score"])
            }
        )

    return documents