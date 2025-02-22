🤖 HR Chatbot - AI-Powered Slack Integration
A GPT-4-powered HR chatbot that automates HR queries using OpenAI, Azure Cognitive Services, and Slack API. This chatbot helps employees get quick answers to common HR questions via Slack.

📌 Features
✅ AI-Powered Responses - Uses GPT-4 for intelligent HR query resolution.
✅ Slack Integration - Employees can interact with the bot directly in Slack.
✅ Document Search - Extracts HR policies using Azure Cognitive Services.
✅ FastAPI Backend - Lightweight, fast, and scalable API service.
✅ Deployed on Render - Ensures easy deployment and hosting.

📁 Project Structure

gen_ai_chatbot/
│── hr_documents/            # HR policy documents (text & PDF)
│── .env                     # API keys & environment variables (DO NOT COMMIT)
│── chatbot_api.py           # FastAPI backend
│── chatbot_ui.py            # Streamlit frontend (if required)
│── azure_text_analysis.py   # Azure Cognitive Services integration
│── read_documents.py        # HR document retrieval logic
│── requirements.txt         # Python dependencies
│── README.md                # Project documentation
🚀 Deployment Steps
Follow the steps below to deploy the chatbot locally and on Slack.

1️⃣ Setup Locally
🔹 Step 1: Clone the Repository
        git clone https://github.com/himanu-dandle/genai_chatbot.git
        cd genai_chatbot
🔹 Step 2: Create Virtual Environment & Install Dependencies
        python -m venv genai_hr_chatbot_env
        source genai_hr_chatbot_env/bin/activate  # Mac/Linux
        genai_hr_chatbot_env\Scripts\activate    # Windows

        pip install -r requirements.txt
🔹 Step 3: Set Environment Variables
    Create a .env file in the root directory and add:
    OPENAI_API_KEY="your-openai-api-key"
    AZURE_TEXT_ANALYTICS_KEY="your-azure-key"
    AZURE_TEXT_ANALYTICS_ENDPOINT="your-azure-endpoint"
    SLACK_BOT_TOKEN="xoxb-your-slack-bot-token"
🔹 Step 4: Run the API
    uvicorn chatbot_api:app --reload
🔹 Your API will be available at:
👉 http://127.0.0.1:8000
👉 API Docs: http://127.0.0.1:8000/docs

2️⃣ Slack App Configuration
🔹 Step 1: Create a Slack App
1️⃣ Go to Slack API Apps.
2️⃣ Click "Create New App" → Choose "From Scratch".
3️⃣ Enter an App Name (e.g., HR Chatbot) and select your workspace.

🔹 Step 2: Configure OAuth & Permissions
1️⃣ Go to "OAuth & Permissions" in your Slack App settings.
2️⃣ Scroll down to "Scopes" and add the following Bot Token Scopes:

OAuth Scope	Description
app_mentions:read	Detect when bot is mentioned
calls:write	Start & manage calls
channels:read	Read public channels
chat:write	Send messages in Slack
commands	Add ortcuts/sla commands
groups:read	Read private channels bot has access to
im:history	Read direct messages bot has access to
im:read	View basic DM info
im:write	Start DMs with users
mpim:read	Read group DMs bot has access to
3️⃣ Click Save Changes.

🔹 Step 3: Install the App to Your Workspace
1️⃣ Scroll up and click "Install to Workspace".
2️⃣ Click Allow to grant permissions.
3️⃣  the Bot User OAuth Token (xoxb-...) and add it to your .env file:


SLACK_BOT_TOKEN="xoxb-your-slack-token"
🔹 Step 4: Enable Event Subscriptions
1️⃣ Go to "Event Subscriptions" in Slack App settings.
2️⃣ Toggle "Enable Events" → ON.
3️⃣ In "Request URL", enter:


https://genai-chatbot-3uqj.onrender.com/slack/events
4️⃣ Click Verify → Ensure Verified status appears.
5️⃣ Scroll to "Subscribe to Bot Events" and add:

Event Name	    Description	                                Required Scope
app_mention	    Detects when users mention @HR Chatbot	    app_mentions:read
message.im	    Detects messages sent in direct messages	im:history
6️⃣ Click Save Changes.

🔹 Step 5: Invite Bot to a Slack Channel
1️⃣ Open Slack.
2️⃣ Navigate to a channel (e.g., #general).
3️⃣ Type:/invite @HR Chatbot
4️⃣ Send a test message:

@HR Chatbot What is the sick leave policy?
3️⃣ Deployment on Render
🔹 Step 1: Create a Render Web Service
1️⃣ Go to Render.
2️⃣ Click "New Web Service" → Connect GitHub repository.
3️⃣ Select your HR Chatbot repository.
4️⃣ Set environment variables in Render Daboard:

OPENAI_API_KEY=your-openai-api-key
AZURE_TEXT_ANALYTICS_KEY=your-azure-key
AZURE_TEXT_ANALYTICS_ENDPOINT=your-azure-endpoint
SLACK_BOT_TOKEN=xoxb-your-slack-bot-token
5️⃣ Set Start Command:
    uvicorn chatbot_api:app --host 0.0.0.0 --port $PORT
6️⃣ Click Deploy.

📌 Once deployed, your API will be accessible at:
🔹 https://genai-chatbot-3uqj.onrender.com

✅ Testing
🔹 Slack Bot API Test
Run the following command:
curl -k -X POST "https://slack.com/api/chat.postMessage" ^
-H "Authorization: Bearer xoxb-your-slack-token" ^
-H "Content-Type: application/json" ^
-d "{ \"channel\": \"YOUR_CHANNEL_ID\", \"text\": \"Hello from my bot!\" }"
🔹 Expected Output:{ "ok": true, "channel": "C08DVTGCQ", "message": { "text": "Hello from my bot!" } }

🔧 Troubleooting
🔸 Slack Bot Not Responding?
✔ Ensure bot is invited to the channel.
✔ Verify event subscriptions are configured correctly.
✔ Restart the bot by redeploying on Render.

🔸 Slack Bot Token Not Working?
✔ Reinstall the Slack App and generate a new token.
✔ Add the correct permissions in OAuth & Permissions.

📜 License
MIT License - Free to use and modify.

