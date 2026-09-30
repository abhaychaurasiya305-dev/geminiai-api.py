import os
from dotenv import load_dotenv
from google import genai

# 1. Load variables from .env file
load_dotenv()

# 2. Read Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

# 3. Check whether API key exists
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the .env file.")

# 4. Initialize the Gemini client
client = genai.Client(api_key=api_key)

# 5. Send prompt to Gemini
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explain Generative AI in simple terms for a beginner."
)

# 6. Print the result
print(response.text)