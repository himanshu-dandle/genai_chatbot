import openai
import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from pydantic import BaseModel
from read_documents import search_policy_documents
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# ✅ Load API keys from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
slack_token = os.getenv("SLACK_BOT_TOKEN")

# ✅ Initialize FastAPI
app = FastAPI()

# ✅ Initialize Slack Client
slack_client = WebClient(token=slack_token)

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

    try:
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an HR assistant. Use only the provided policy."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200
        )
        return response.choices[0].message.content  # ✅ Extract the correct response
    except Exception as e:
        print(f"❌ OpenAI API Error: {e}")
        return "⚠️ Error generating a response. Please try again later."

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

# ✅ Slack Event API Route
@app.post("/slack/events")
async def slack_events(request: Request):
    payload = await request.json()
    event = payload.get("event", {})

    if event.get("type") == "app_mention":
        user_message = event.get("text", "")
        channel_id = event.get("channel")

        # 🔍 Debugging: Print the received Slack message
        print(f"🔹 Slack Message Received: {user_message}")

        # Get GPT-4 response
        policy_answer = search_policy_documents(user_message.lower().split())
        bot_reply = generate_gpt4_response(user_message, policy_answer)

        # Send reply to Slack
        try:
            slack_client.chat_postMessage(channel=channel_id, text=bot_reply)
        except SlackApiError as e:
            print(f"❌ Slack API Error: {e.response['error']}")

    return {"status": "ok"}

# ✅ Root endpoint
@app.get("/")
def home():
    return {"message": "HR Chatbot API with GPT-4 is running!"}
