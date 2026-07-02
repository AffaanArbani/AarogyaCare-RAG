"""
Test the complete RAG pipeline.
"""

from chatbot.rag import chat

SESSION_ID = "demo_session"

print("=" * 70)
print("AarogyaCare RAG Chatbot")
print("Type 'exit' to quit.")
print("=" * 70)

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    answer = chat(
        session_id=SESSION_ID,
        question=question
    )

    print("\nBot:\n")
    print(answer)