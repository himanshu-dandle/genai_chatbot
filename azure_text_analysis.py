import os
from dotenv import load_dotenv
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# ✅ Load API keys from .env
load_dotenv()
AZURE_API_KEY = os.getenv("AZURE_TEXT_ANALYTICS_KEY")
AZURE_ENDPOINT = os.getenv("AZURE_TEXT_ANALYTICS_ENDPOINT")

# ✅ Validate API Key & Endpoint
if not AZURE_API_KEY or not AZURE_ENDPOINT:
    raise ValueError("❌ ERROR: Missing Azure API Key or Endpoint. Check your .env file.")

# ✅ Create Azure Text Analytics Client
def authenticate_client():
    return TextAnalyticsClient(endpoint=AZURE_ENDPOINT, credential=AzureKeyCredential(AZURE_API_KEY))

client = authenticate_client()

# ✅ Function to analyze key phrases
def extract_key_phrases(text):
    try:
        response = client.extract_key_phrases([text])
        if response and response[0] and not response[0].is_error:
            return response[0].key_phrases
        else:
            return f"⚠️ Error: {response[0].error}" if response else "⚠️ Error: No response received from API."
    except Exception as e:
        return f"❌ Exception Occurred: {e}"

# ✅ Test the function
if __name__ == "__main__":
    sample_text = "How many paid leave days do I have?"
    key_phrases = extract_key_phrases(sample_text)
    print("🔍 Key Phrases Extracted:", key_phrases)
