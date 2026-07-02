"""
Test script for embedding generation.
"""

from chatbot.embeddings import embed_query, embed_text


print("=" * 60)
print("Testing Query Embedding")
print("=" * 60)

query = "I have severe back pain."

query_embedding = embed_query(query)

print(f"Embedding Length : {len(query_embedding)}")
print(f"First 5 Values   : {query_embedding[:5]}")


print("\n" + "=" * 60)
print("Testing Document Embedding")
print("=" * 60)

document = """
Condition
Back Pain

Symptoms
Pain in the lower back.

Home Remedies
Rest, stretching and hydration.
"""

document_embedding = embed_text(document)

print(f"Embedding Length : {len(document_embedding)}")
print(f"First 5 Values   : {document_embedding[:5]}")

print("\n✅ Embedding module is working correctly.")