import requests
from dotenv import load_dotenv
import os
#loading environment variables from .env file
load_dotenv()
API_KEY = "zdk2syKvr93zfob9qOYmnReNnw01ceAy"
IP = "8.8.8.8"
URL = f"https://api.shodan.io/shodan/host/{IP}?key={API_KEY}"
response = requests.get(URL)
print(response.json())