import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("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")

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "Write a Python function to calculate factorial"},
    ]
)

print(response['choices'][0]['message']['content'])
