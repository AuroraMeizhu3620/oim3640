# import requests
# from pprint import pprint
# from dotenv import load_dotenv
# import os

# load_dotenv()

# print(url)
# data = requests.get(url).json()
# print(len(data))
# print(data.keys())
# city = input("Enter city:")
# print(f"{city}:{data['main']['temp']}°F")

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-5-nano",
    messages=[
        {"role": "user", "content": "write a one-sentence bedtime story about a unicorn"}
    ]
)

print(response.choices[0].message.content)