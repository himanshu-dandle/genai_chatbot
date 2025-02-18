import requests

# Azure Credentials
AZURE_ENDPOINT = "https://hr-text-analytics-new.cognitiveservices.azure.com/"
AZURE_API_KEY = "1Hophh5N9UMTWuiUHNljydqN5fq8kcCzn9XKf895dUaTmjYpGW2tJQQJ99BBACYeBjFXJ3w3AAAAACOGG9vd"

# Use API v3.1 (since v3.2-preview.2 is not supported in S0)
url = AZURE_ENDPOINT + "text/analytics/v3.1/keyPhrases"

# Request Headers
headers = {
    "Ocp-Apim-Subscription-Key": AZURE_API_KEY,
    "Content-Type": "application/json"
}

# Request Data
data = {
    "documents": [
        {"id": "1", "language": "en", "text": "I need information about my paid leave policy."}
    ]
}

# Make API Request
response = requests.post(url, headers=headers, json=data)

# Print Response
print("Response Status Code:", response.status_code)
print("Response JSON:", response.json())
