import requests
import psycopg2
from dotenv import load_dotenv
import os
#loading environment variables from .env file
load_dotenv()
API_KEY = "***************"
IP = "8.8.8.8"
ports = [80, 443]
services = ["HTTP", "HTTPS"]
URL = f"https://api.shodan.io/shodan/host/{IP}?key={API_KEY}"
response = requests.get(URL)
#Store the data in the database
conn = psycopg2.connect(dbname="defaultdb",
                        user = "doadmin",
                        host="**********",
                        port="25060",
                        password="************"
                        )
cursor = conn.cursor()
cursor.execute(
       "INSERT INTO threat_data (ip_address, ports, services) VALUES (%s, %s, %s)",
    ((IP, ports, services) ))
conn.commit()
cursor.close()
conn.close()
print(response.json())
