import requests
from dotenv import load_dotenv
import os

load_dotenv()

Weather_KEY = os.getenv("7443b63f8f36239daa4156569e1b4959")
# data = requests.get(Weather_KEY).json()
# print(len(data))
# print(data.keys())
# city = input("Enter city:")
# print(f"{city}:{data['main']['temp']}°F")
