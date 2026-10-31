from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

interaction = client.interactions.create(
    model="gemini-3.6-flash",  # agar 503 aaye to gemini-3.5-flash-lite kar dena
    input="Age of Earth."
)

print(interaction.output_text)