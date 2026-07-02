import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load .env
load_dotenv()

# Initialize Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0
)

# Ask a test question
response = llm.invoke("Hello! Tell me about yourself in 2 sentences.")

print("\nGemini Response:\n")
print(response.content)