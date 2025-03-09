import requests
from dotenv import load_dotenv
import os
API_KEY = "51abcad742518c310918dd5bbd831e67e15d11bba3827285c3a3c50400c7f8d4"
IP = "8.8.8.8"  # You can also use a file hash instead of an IP
URL = f"https://www.virustotal.com/api/v3/ip_addresses/{IP}"

headers = {
    "x-apikey": API_KEY
}

response = requests.get(URL, headers=headers)
print(response.json())
