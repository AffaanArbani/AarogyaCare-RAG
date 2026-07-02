import os
import re
from dotenv import load_dotenv

from pinecone import Pinecone
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
from langchain_pinecone import PineconeVectorStore

load_dotenv()

# ----------------------------
# Initialize Gemini Embeddings
# ----------------------------
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# ----------------------------
# Connect to Pinecone
# ----------------------------
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index_name = os.getenv("PINECONE_INDEX")

vector_store = PineconeVectorStore(
    index_name=index_name,
    embedding=embeddings
)

# ----------------------------
# Read Dataset
# ----------------------------
with open("data/disease_data.txt", "r", encoding="utf-8") as f:
    text = f.read()

# ----------------------------
# Split into diseases
# ----------------------------
sections = re.split(r"\nCondition\s*\n", text)

documents = []

for section in sections:

    section = section.strip()

    if not section:
        continue

    lines = section.split("\n")

    disease = lines[0].strip()

    document = Document(
        page_content=section,
        metadata={
            "disease": disease
        }
    )

    documents.append(document)

print(f"\nFound {len(documents)} diseases.\n")

# ----------------------------
# Upload to Pinecone
# ----------------------------
vector_store.add_documents(documents)

print("✅ Upload Complete!")