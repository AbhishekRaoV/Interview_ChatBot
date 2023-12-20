import requests

ACCESS_TOKEN = "ya29.a0AfB_byDXkzVC_dhCmM5kDpE3lVd7cpsgvwjP7ecuSJbEVutp8lmYkBcItJw4JgAMFM9OB-veTUrxI5lrE2VctYNO2ZubXlns_mBLcnb1KKo2oZ0poOMNLu8dCYTEYFq9CGNJ8BtySdqCs270ybD9SFW4Larv8ySXAUe8mGMNawaCgYKAekSARISFQHGX2MiDv3NwsG2LaG2X4EODS2sRA0177"
API_ENDPOINT = "us-central1-aiplatform.googleapis.com"
PROJECT_ID = "arena-challenge"
MODEL_ID = "text-bison"
LOCATION_ID = "us-central1"

# Add text before reading content from the user_input.txt file
prefix_text = "perform sentiment analysis on the following text. only give me positive or negative no extra explanation"
file_path = "user_input.txt"

with open(file_path, "r", encoding="utf-8") as file:
    user_input_content = file.read()

# Combine the prefix and file content
content = prefix_text + user_input_content

url = f"https://{API_ENDPOINT}/v1/projects/{PROJECT_ID}/locations/{LOCATION_ID}/publishers/google/models/{MODEL_ID}:predict"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",
}

data = {
    "instances": [
        {
            "content": content
        }
    ],
    "parameters": {
        "candidateCount": 1,
        "maxOutputTokens": 1024,
        "temperature": 0.2,
        "topP": 0.8,
        "topK": 40
    }
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    sentiment_label = result["predictions"][0]["content"].strip().lower()  # Extract sentiment label
    print(f"Sentiment: {sentiment_label}")
else:
    print(f"Error: {response.status_code} - {response.text}")

with open("user_input.txt", "a") as file:
        file.write(f"Sentiment: {sentiment_label}\n")
