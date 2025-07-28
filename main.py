import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
print("API key loaded:", os.getenv("OPENAI_API_KEY"))


response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Write a Python function to calculate factorial"},
    ]
)

print(response.choices[0].message.content)
