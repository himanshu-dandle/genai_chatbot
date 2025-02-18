from fastapi import FastAPI
from chatbot_api import ask_question  # Import from chatbot API

# Initialize FastAPI app
app = FastAPI()

# Home endpoint
@app.get("/")
def home():
    return {"message": "HR Chatbot API is running!"}

# Expose chatbot API through FastAPI
@app.post("/ask")
def ask(question: str):
    return ask_question({"question": question})

# Run the app (for local testing)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
