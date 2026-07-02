"""
Test script for Pinecone retrieval.
"""

from chatbot.retriever import retrieve_context

results = retrieve_context(
    "I have severe back pain.",
    top_k=3
)

print("=" * 80)
print("Retrieved Documents")
print("=" * 80)

for i, result in enumerate(results, start=1):

    print(f"\nResult {i}")

    print("-" * 80)

    print(f"Disease : {result['disease']}")

    print(f"Score   : {result['score']:.4f}")

    print()

    print(result["text"][:500])

print("\n✅ Retriever module is working correctly.")