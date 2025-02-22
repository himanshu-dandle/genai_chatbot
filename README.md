# 🤖 ***AI-Powered HR Chatbot (Slack Integration)***  

![GitHub repo size](https://img.shields.io/github/repo-size/himanshu-dandle/genai_chatbot?style=flat)  
![GitHub contributors](https://img.shields.io/github/contributors/himanshu-dandle/genai_chatbot?color=blue)  
![GitHub last commit](https://img.shields.io/github/last-commit/himanshu-dandle/genai_chatbot)  


💬 **Live Chatbot Demo:** 👉 *Coming Soon*  
💻 **GitHub Repository:** 👉 [genai_chatbot](https://github.com/himanshu-dandle/genai_chatbot)  

---

## 📌 ***Project Overview***  

🚀 ***AI-Powered HR Chatbot*** that automates employee queries using ***GPT-4, Azure Cognitive Services, and Slack API.*** The chatbot provides ***real-time HR assistance, document-based query retrieval, and seamless Slack integration.***  

### ✅ ***Key Features:***  

✔ ***AI-Powered Responses*** – Uses ***GPT-4*** for intelligent HR query resolution.  
✔ ***Slack Integration*** – Employees can interact with the bot directly in ***Slack***.  
✔ ***Document Search*** – Extracts HR policies using ***Azure Cognitive Services***.  
✔ ***FastAPI Backend*** – Lightweight, fast, and scalable API service.  
✔ ***Deployed on Render*** – Ensures easy deployment and hosting.  

---

## 🏗 ***Tech Stack Used***  

| ***Technology***          | ***Usage***                                |
|----------------------|-----------------------------------------|
| ***Python***        | Programming Language                    |
| ***OpenAI GPT-4***  | AI-powered chatbot responses            |
| ***Azure AI Services*** | HR document search & text analysis    |
| ***FastAPI***       | Backend API framework                   |
| ***Uvicorn***       | ASGI server for FastAPI                 |
| ***Slack API***     | Slack integration for chatbot           |
| ***Render***        | Cloud deployment for API & services      |

---

## 📂 ***Project Structure***  

```
gen_ai_chatbot/
│── hr_documents/            # HR policy documents (text & PDF)
│── .env                     # API keys & environment variables (DO NOT COMMIT)
│── chatbot_api.py           # FastAPI backend
│── chatbot_ui.py            # Streamlit frontend (if required)
│── azure_text_analysis.py   # Azure Cognitive Services integration
│── read_documents.py        # HR document retrieval logic
│── requirements.txt         # Python dependencies
│── README.md                # Project documentation



🛠 How to Run the Chatbot Locally
✅ 1. Clone the Repository


git clone https://github.com/himanu-dandle/genai_chatbot.git
cd genai_chatbot
✅ 2. Create Virtual Environment & Install Dependencies


python -m venv genai_hr_chatbot_env
source genai_hr_chatbot_env/bin/activate  # Mac/Linux
genai_hr_chatbot_env\Scripts\activate    # Windows

pip install -r requirements.txt
✅ 3. Set Environment Variables
Create a .env file in the root directory and add:


OPENAI_API_KEY="your-openai-api-key"
AZURE_TEXT_ANALYTICS_KEY="your-azure-key"
AZURE_TEXT_ANALYTICS_ENDPOINT="your-azure-endpoint"
SLACK_BOT_TOKEN="xoxb-your-slack-bot-token"
✅ 4. Run the FastAPI Backend


uvicorn chatbot_api:app --reload
🔹 API will be available at:
👉 http://127.0.0.1:8000
👉 API Docs: http://127.0.0.1:8000/docs

📢 Slack Bot Integration
✅ 1. Create a Slack App
1️⃣ Go to Slack API Apps.
2️⃣ Click "Create New App" → Choose "From Scratch".
3️⃣ Enter an App Name (e.g., HR Chatbot) and select your workspace.

✅ 2. Configure OAuth & Permissions
🔹 Go to "OAuth & Permissions" in your Slack App settings.
🔹 Scroll down to "Scopes" and add the following Bot Token Scopes:

OAuth Scope	Description
app_mentions:read	Detect when bot is mentioned
calls:write	Start & manage calls
channels:read	Read public channels
chat:write	Send messages in Slack
commands	Add shortcuts/slash commands
groups:read	Read private channels bot has access to
im:history	Read direct messages bot has access to
im:read	View basic DM info
im:write	Start DMs with users
mpim:read	Read group DMs bot has access to
🔹 Click Save Changes.

🚀 Deploying on Render
✅ 1. Deploy Backend on Render
1️⃣ Go to Render.
2️⃣ Click "New Web Service" → Connect GitHub repository.
3️⃣ Select your HR Chatbot repository.
4️⃣ Set environment variables in Render Dashboard:



OPENAI_API_KEY=your-openai-api-key
AZURE_TEXT_ANALYTICS_KEY=your-azure-key
AZURE_TEXT_ANALYTICS_ENDPOINT=your-azure-endpoint
SLACK_BOT_TOKEN=xoxb-your-slack-bot-token
5️⃣ Set Start Command:



uvicorn chatbot_api:app --host 0.0.0.0 --port $PORT
6️⃣ Click Deploy.

📌 Once deployed, your API will be accessible at:
🔹 https://genai-chatbot-3uqj.onrender.com

🔍 Testing the Slack Bot API
Run the following command:



curl -k -X POST "https://slack.com/api/chat.postMessage" \
-H "Authorization: Bearer xoxb-your-slack-token" \
-H "Content-Type: application/json" \
-d '{ "channel": "YOUR_CHANNEL_ID", "text": "Hello from my bot!" }'
✅ Expected Output:


{
    "ok": true,
    "channel": "C08DVTGCQ",
    "message": { "text": "Hello from my bot!" }
}
🔧 Troubleshooting
🔹 Slack Bot Not Responding?
✔ Ensure the bot is invited to the channel.
✔ Verify event subscriptions are correctly configured.
✔ Restart the bot by redeploying on Render.

🔹 Slack Bot Token Not Working?
✔ Reinstall the Slack App and generate a new token.
✔ Add the correct permissions in OAuth & Permissions.

📜 License
📝 MIT License - Free to use and modify.

🌟 If you like this project, give it a ⭐ on GitHub! 🚀

