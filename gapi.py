import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Initialize the client and authenticate with the API

client = genai.Client(api_key = os.getenv("OPEN_API_KEY"))

# send the prompt to the model

response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = "Explain to me how does a gemini Api work in one sentence"
)

# print the  result to the terminal
print(response.text)