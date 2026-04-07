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

# load_dotenv()
# client = OpenAI()

# response = client.chat.completions.create(
#     model="gpt-5-nano",
#     messages=[
#         {"role": "user", 
#          "content": "write a one-sentence bedtime story about a unicorn"}
#     ]
# )

# print(response.choices[0].message.content)

load_dotenv()

client = OpenAI() 
conversation_history = []

print("Chatbot: Hello! I'm your AI assistant. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()
    
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    
    if not user_input:
        continue
        
    conversation_history.append({
        "role": "user",
        "content": user_input
    })
    
    response = client.chat.completions.create(
        model="gpt-4-mini",
        messages=conversation_history
    )
    
    assistant_message = response.choices[0].message.content
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })
    
    print(f"Chatbot: {assistant_message}\n")