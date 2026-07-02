"""
Configuration module for the AarogyaCare RAG Chatbot.

This module initializes and exposes:

- Environment variables
- Sentence Transformer embedding model
- Pinecone vector database
- Google Gemini client
- Redis client

These resources are loaded only once and reused throughout the application.
"""

import os

import redis
from dotenv import load_dotenv
from google import genai
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer

# ==========================================================
# Load Environment Variables
# ==========================================================

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_DB = int(os.getenv("REDIS_DB", 0))

EMBEDDING_MODEL_NAME = os.getenv(
    "EMBEDDING_MODEL",
    "sentence-transformers/all-MiniLM-L6-v2"
)

GEMINI_MODEL_NAME = os.getenv(
    "GEMINI_MODEL",
    "gemini-2.5-flash"
)

# ==========================================================
# Initialize Gemini Client
# ==========================================================

gemini_client = genai.Client(
    api_key=GOOGLE_API_KEY
)

# ==========================================================
# Load Sentence Transformer
# ==========================================================

embedding_model = SentenceTransformer(
    EMBEDDING_MODEL_NAME
)

# ==========================================================
# Connect to Pinecone
# ==========================================================

pinecone = Pinecone(
    api_key=PINECONE_API_KEY
)

pinecone_index = pinecone.Index(
    PINECONE_INDEX
)

# ==========================================================
# Connect to Redis
# ==========================================================


print("=" * 50)
print(f"REDIS_HOST = {REDIS_HOST}")
print(f"REDIS_PORT = {REDIS_PORT}")
print(f"REDIS_DB = {REDIS_DB}")
print("=" * 50)

redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_DB,
    decode_responses=True
)