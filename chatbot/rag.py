"""
Core Retrieval-Augmented Generation (RAG) pipeline
for the AarogyaCare chatbot.
"""

import time

from chatbot.config import gemini_client, GEMINI_MODEL_NAME
from chatbot.memory import (
    get_chat_history,
    save_message,
)
from chatbot.prompts import SYSTEM_PROMPT
from chatbot.retriever import retrieve_context


def build_prompt(
    question: str,
    context: list[dict],
    history: list[dict]
) -> str:
    """
    Build the prompt using conversation history
    and retrieved medical context.
    """

    # -------------------------------
    # Conversation History
    # -------------------------------

    if history:
        history_text = "\n".join(
            f"{message['role'].capitalize()}: {message['message']}"
            for message in history
        )
    else:
        history_text = "No previous conversation."

    # -------------------------------
    # Retrieved Context
    # -------------------------------

    context_text = ""

    for document in context:
        context_text += f"""

Disease:
{document['disease']}

Medical Information:
{document['text']}

------------------------------------------------------------
"""

    # -------------------------------
    # Final Prompt
    # -------------------------------

    prompt = f"""
{SYSTEM_PROMPT}

==================================================
Conversation History
==================================================

{history_text}

==================================================
Retrieved Medical Context
==================================================

{context_text}

==================================================
User Question
==================================================

{question}

==================================================
Instructions
==================================================

Answer naturally as if you're chatting with the user.

Use ONLY the retrieved medical information.

If the user's exact question is not answered in the retrieved context:

- Do not invent information.
- Explain that the specific information isn't available.
- Then provide any closely related guidance that IS available.

Keep the response concise.

Avoid sounding like a medical report.

Never recommend medications or dosage.

Focus on safe home remedies, hydration, rest, lifestyle advice, prevention, and guidance on when professional medical care should be sought.

Only recommend consulting a healthcare professional when appropriate based on the retrieved medical information.
"""

    return prompt.strip()


def generate_response(prompt: str) -> str:
    """
    Generate a response using Gemini.
    Automatically retries if the API is temporarily unavailable.
    """

    for attempt in range(3):

        try:

            response = gemini_client.models.generate_content(
                model=GEMINI_MODEL_NAME,
                contents=prompt,
            )

            return response.text.strip()

        except Exception as e:

            print(f"Attempt {attempt + 1} failed: {e}")

            if attempt < 2:
                time.sleep(3)

            else:
                return (
                    "I'm sorry, I'm temporarily unable to respond because "
                    "the AI service is experiencing heavy traffic. "
                    "Please try again in a few moments."
                )


def chat(
    session_id: str,
    question: str
) -> str:
    """
    Complete RAG pipeline.
    """

    # Retrieve previous conversation
    history = get_chat_history(session_id)

    # Retrieve relevant medical documents
    context = retrieve_context(
        query=question,
        top_k=2
    )

    # Build prompt
    prompt = build_prompt(
        question=question,
        context=context,
        history=history,
    )

    # Generate response
    answer = generate_response(prompt)

    # Save user message
    save_message(
        session_id=session_id,
        role="user",
        message=question,
    )

    # Save assistant response
    save_message(
        session_id=session_id,
        role="assistant",
        message=answer,
    )

    return answer