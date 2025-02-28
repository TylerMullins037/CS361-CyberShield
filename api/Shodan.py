import requests
API_KEY = "zdk2syKvr93zfob9qOYmnReNnw01ceAy"
IP = "8.8.8.8"
URL = f"https://api.shodan.io/shodan/host/{IP}?key={API_KEY}"
response = requests.get(URL)
print(response.json())