
import psycopg2
import shodan
import requests
from time import sleep


SHODAN_API_KEY = "***********"
SECURITY_TRAILS_API_KEY = "*************"
VIRUS_TOTAL_API_KEY = "***********"


DB_HOST = "**************"
DB_NAME = "defaultdb"
DB_USER = "doadmin"
DB_PASS = "**********"

# Fetch data from Shodan
def fetch_shodan_data(ip_address):
    try:
        api = shodan.Shodan(SHODAN_API_KEY)
        response = api.host(ip_address)  # Fetch data for the ip address
        return response
    except shodan.APIError as e:
        print(f"Shodan API error: {e}")
        return None

# Fetch data from SecurityTrails
def fetch_security_data(domain):
    url = f"https://api.securitytrails.com/v1/domain/{domain}"
    headers = {"APIKEY": SECURITY_TRAILS_API_KEY}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else None

# Fetch data from VirusTotal
def fetch_virus_total_data(ip_address):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip_address}"
    headers = {"x-apikey": VIRUS_TOTAL_API_KEY}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else None

# Store threat intelligence data into Database
def store_threat_intelligence(threat_name, vulnerability, likelihood, impact, risk_score):
    try:
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS,
                                host=DB_HOST,port="25060",
                                sslmode="require")
        cursor = conn.cursor()

        # Insert data
        cursor.execute("""
            INSERT INTO tva_mapping (threat_name, vulnerability_description, likelihood, impact, risk_score)
            VALUES (%s, %s, %s, %s, %s)
        """, (threat_name, vulnerability, likelihood, impact, risk_score))
        conn.commit()

        # check for insertion
        cursor.execute("SELECT * FROM tva_mapping WHERE threat_name = %s", (threat_name,))
        rows = cursor.fetchall()
        if rows:
            print("Data inserted successfully:", rows)

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error storing the data: {e}")

# Main function
def main():
    print("Begin of the main function...")
    domain = "google.com"
    ip_address = "8.8.8.8"

    # Fetch and process Shodan data
    shodan_data = fetch_shodan_data(ip_address)
    if shodan_data:
        ports = shodan_data.get("ports", [])
        store_threat_intelligence(
            threat_name="Exposed Ports",
            vulnerability=f"Exposed ports: {', '.join(map(str, ports))}",
            likelihood=4,
            impact=5,
            risk_score=4 * 5
        )

    # Fetch and process VirusTotal data
    virus_data = fetch_virus_total_data(ip_address)
    if virus_data and "data" in virus_data:
        attributes = virus_data["data"]["attributes"]
        threat_score = attributes.get("reputation", "N/A")
        store_threat_intelligence(
            threat_name="VirusTotal Reputation",
            vulnerability=f"Domain reputation score: {threat_score}",
            likelihood=3,
            impact=4,
            risk_score=3 * 4
        )

    # Fetch and process SecurityTrails data
    security_data = fetch_security_data(domain)
    if security_data:
        for record in security_data.get("records", []):
            store_threat_intelligence(
                threat_name="DNS Records",
                vulnerability=f"DNS record: {record}",
                likelihood=2,
                impact=4,
                risk_score=2 * 4
            )


while True:
    main()
    print("Wait for for me please. I take a rest for 2 hours")
    sleep(7200) 

