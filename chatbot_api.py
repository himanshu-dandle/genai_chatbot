import openai
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from read_documents import search_policy_documents

# ✅ Load API key securely from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# ✅ Initialize FastAPI
app = FastAPI()

# ✅ Request model
class QueryRequest(BaseModel):
    question: str

# ✅ Function to generate GPT-4 response using HR policy text
def generate_gpt4_response(question, policy_answer):
    prompt = f"""
    You are an HR chatbot. The user asked: "{question}".
    Here is the official company policy: "{policy_answer}".
    Always answer using this policy. If the policy does not mention something, say "I don't have information on that."
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an HR assistant. Use only the provided policy."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200
    )

    return response["choices"][0]["message"]["content"]

# ✅ API endpoint for chatbot queries
@app.post("/ask")
def ask_question(request: QueryRequest):
    key_phrases = request.question.lower().split()
    policy_answer = search_policy_documents(key_phrases)

    # 🔍 Debugging: Print extracted HR policy
    print("\n🔍 DEBUG: Extracted Policy Text →", policy_answer, "\n")

    if not policy_answer or "⚠️ No relevant policy found" in policy_answer:
        return {"question": request.question, "answer": "I couldn't find a policy related to your question."}

    gpt4_response = generate_gpt4_response(request.question, policy_answer)
    
    return {"question": request.question, "answer": gpt4_response}


# ✅ Root endpoint
@app.get("/")
def home():
    return {"message": "HR Chatbot API with GPT-4 is running!"}
