"""
Frontend for the AarogyaCare RAG Chatbot.
"""

import os
import uuid
import requests
import streamlit as st

# ============================================
# Page Configuration
# ============================================

st.set_page_config(
    page_title="AarogyaCare",
    page_icon="🩺",
    layout="wide"
)

# ============================================
# Backend URL
# ============================================

API_URL = os.getenv(
    "BACKEND_URL",
    "http://127.0.0.1:8000"
)

print("=" * 50)
print(f"API_URL = '{API_URL}'")
print(f"CHAT_URL = '{API_URL}/chat'")
print("=" * 50)

# ============================================
# Session State
# ============================================

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

# ============================================
# Sidebar
# ============================================

with st.sidebar:

    st.title("🩺 AarogyaCare")

    st.markdown("---")

    if st.button("New Conversation", use_container_width=True):

        requests.delete(
            f"{API_URL}/chat/{st.session_state.session_id}"
        )

        st.session_state.messages = []
        st.session_state.session_id = str(uuid.uuid4())

        st.rerun()

    st.markdown("---")

    st.subheader("Technology")

    st.write("• Gemini")
    st.write("• Sentence Transformers")
    st.write("• Pinecone")
    st.write("• Redis")
    st.write("• FastAPI")

# ============================================
# Main Page
# ============================================

st.title("🩺 AarogyaCare")

st.caption("AI-powered Healthcare Assistant")

# Display previous messages

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ============================================
# User Input
# ============================================

prompt = st.chat_input("Type your message...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = requests.post(

                f"{API_URL}/chat",

                json={
                    "session_id": st.session_state.session_id,
                    "message": prompt
                }

            )

            if response.status_code == 200:

                answer = response.json()["response"]

            else:

                answer = f"Error: {response.status_code}\n\n{response.text}"

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )