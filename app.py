"""
Frontend for the AarogyaCare RAG Chatbot.
"""

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
            f"http://127.0.0.1:8000/chat/{st.session_state.session_id}"
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

# User input

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

                "http://127.0.0.1:8000/chat",

                json={
                    "session_id": st.session_state.session_id,
                    "message": prompt
                }

            )

            answer = response.json()["response"]

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )