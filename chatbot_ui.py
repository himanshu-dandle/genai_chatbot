import streamlit as st
import requests  # ✅ Use requests to call FastAPI

# ✅ FastAPI URL (Ensure this matches your FastAPI backend)
FASTAPI_URL = "http://127.0.0.1:8000/ask"

# Web App UI
st.set_page_config(page_title="HR Chatbot", page_icon="🤖")
st.title("💬 HR Chatbot")
st.write("Ask me anything about HR policies!")

# User Input
question = st.text_input("Type your question here:")

# Function to get response from FastAPI
def get_chatbot_response(user_question):
    try:
        response = requests.post(FASTAPI_URL, json={"question": user_question})
        
        # 🔍 Debugging: Print API response
        print("\n🔍 DEBUG: API Response Status Code →", response.status_code)
        print("\n🔍 DEBUG: API Response JSON →", response.json())

        if response.status_code == 200:
            return response.json().get("answer", "⚠️ No answer found.")
        else:
            return "⚠️ Error: Could not connect to chatbot API."
    
    except Exception as e:
        return f"⚠️ Error: {e}"

# If user asks a question, generate response
if st.button("Ask"):
    if question:
        with st.spinner("Thinking... 🤔"):
            answer = get_chatbot_response(question)
            st.success(answer)
    else:
        st.warning("Please enter a question first!")
