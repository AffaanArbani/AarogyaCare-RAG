from chatbot.config import (
    embedding_model,
    gemini_client,
    pinecone_index,
    redis_client
)

print("=" * 60)
print("Embedding Model")
print("=" * 60)
print(embedding_model)

print("\n" + "=" * 60)
print("Gemini Client")
print("=" * 60)
print(gemini_client)

print("\n" + "=" * 60)
print("Pinecone")
print("=" * 60)
print(pinecone_index.describe_index_stats())

print("\n" + "=" * 60)
print("Redis")
print("=" * 60)
print(redis_client.ping())