import psycopg2
import shodan
import requests
from time import sleep
import threat_log
import Shodan
import blue_team_defense
import logging
IP_ADDRESS  = "8.8.8.8"
api_keys = Shodan.API_KEY

SECURITY_TRAILS_API_KEY = "VkDrUE5R_Yo_vY8GelgPzEHUSga-CNRM"
VIRUS_TOTAL_API_KEY = "51abcad742518c310918dd5bbd831e67e15d11bba3827285c3a3c50400c7f8d4"


DB_HOST = "db-postgresql-nyc3-21525-do-user-20065838-0.k.db.ondigitalocean.com"
DB_NAME = "defaultdb"
DB_USER = "doadmin"
DB_PORT="25060"
DB_PASS = "*******"
#configuring logging module to display message above Error, warning, Critical
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

#Dictionary of Ips flagged as potentially dangerous
threat_intel_ips = {
    "192.168.1.10": {"source": "VirusTotal", "score": 90}, #flagged by virus total
    "8.8.8.8" : {"source": "Shodan", "ports": [23, 445]}, #comming from shodan showing it has dangerous ports
    "203.0.113.50" : {"source": "SecurityTrails", "flagged":True} # flagged by securityTrails to show it is malicious
}
#IP addresss to never be blocked if even they are detected by the threat intelligence tools
WHITE_LISTED_IPS = ["127.0.0.1", "198.168.0.1", "8.8.8.8"]
#Testing for Database connection
VT_THRESHOLD=75
try:
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,password=DB_PASS,
                             host=DB_HOST, port=DB_PORT,sslmode="require")
    print("The Database connected successfully.")
    conn.close()
except Exception as e:
    print(f'Database connection failed: {e}')

# Fetch data from Shodan
def fetch_shodan_data(ip_address):
    try:
        api = shodan.Shodan(api_keys)
        response = api.host(ip_address)  # Fetch data for the ip address
        return response
    except shodan.APIError as e:
        print(f"Shodan API error: {e}")
        return None

# Fetch data from SecurityTrails
def fetch_security_data(domain):
    url = f"https://api.securitytrails.com/v1/domain/{domain}"
    headers = {"API_KEY": SECURITY_TRAILS_API_KEY}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else None

# Fetch data from VirusTotal
def fetch_virus_total_data(ip_address):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip_address}"
    headers = {"virustotal-apikey": VIRUS_TOTAL_API_KEY}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else None

# Store threat intelligence data into Database
def store_threat_intelligence(threat_name, vulnerability, likelihood, impact, risk_score):
    try:
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS,
                                host=DB_HOST,port=DB_PORT,
                                sslmode="require")
        cursor = conn.cursor()

        #checking if the table exits
        cursor.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE "
                       "table_name ='tva_mapping');")
        #retrieve the next row
        table_exists=cursor.fetchone()[0]

        #check if the table exists
        if not table_exists:
            print("Table 'tva_mapping' does NOT exist! Please create it manually.")
            return

        print(f"Attempting to insert: {threat_name}, {vulnerability}, {likelihood}, {impact}, {risk_score}")

        # Insert data
        cursor.execute("""
            INSERT INTO tva_mapping (threat_name, vulnerability_description, likelihood, impact, risk_score)
            VALUES (%s, %s, %s, %s, %s)
        """, (threat_name, vulnerability, likelihood, impact, risk_score))
        conn.commit()
        print("Data was inserted successfuly")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error storing the data: {e}")

# Main function
def fetch_osint_updates(ip):
    print("Begin of the main function...")
    domain = "google.com"
    for ip, data in threat_intel_ips.items():
        reason = None
        if data["source"] == "VirusTotal" and data.get("score",0) >= VT_THRESHOLD:
            return "VirusTotal Scre {data['score']}".format(data=data)
        #check for threat from Shodan
        elif data["source"] == "Shodan" and  any(p in [23, 445] for p in data.get("ports", [])):
            reason =  "Shodan flagged risk ports: {data['ports']}".format(data=data)
        elif data["source"] == "SecurityTrails"  and data.get("flagged"):
            reason = "SecurityTrails flagged ip as suspicious"
        if reason:
            blue_team_defense.block(ip, reason)

    # Fetch and process Shodan data
    shodan_data = fetch_shodan_data(ip)
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
    virus_data = fetch_virus_total_data(ip)
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

    logging.info("OSINT Threat data fetch complete")



