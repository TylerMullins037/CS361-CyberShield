import requests
API_KEY = "VkDrUE5R_Yo_vY8GelgPzEHUSga-CNRM"
DOMAIN = "umkc.edu"  # You can use a domain instead of an IP
URL = f"https://api.securitytrails.com/v1/domain/{DOMAIN}"

headers = {
    "APIKEY": API_KEY
}

response = requests.get(URL, headers=headers)
print(response.json())