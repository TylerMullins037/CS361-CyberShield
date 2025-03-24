import requests
import psycopg2
from psycopg2 import Error
import time
from risk_prioritization import RiskPrioritizationModel, determine_base_risk,determine_likelihood

def scan_domain(domain, api_key):
    #Scanning the domain for vulnerabilities and storing them in the PostgreSQL database

    URL = f"https://api.securitytrails.com/v1/domain/{domain}"

    headers = {
        "APIKEY": api_key
    }

    def fetch_data_with_security_trails(url, headers, max_retries=10, backoff_factor=2):
        """handles api rate limit  by retring with exponential back off"""
        retries = 0
        while retries < max_retries:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return response.json() #succeed
            elif response.status_code == 429:
                wait_time = (2 ** retries) * backoff_factor
                print(f"Rate limit exceeded, Retrying in {wait_time} seconds")
                #make it sleep
                time.sleep(wait_time)
                retries +=1
            else:
                print(f'API ERROR{response.status_code}: {response.text}')
                return None
        print("maximum limt reached, Skipping API Call")
        return None
    data  = fetch_data_with_security_trails(URL, headers)
    if not data:
        return #exit data was  not fetched

        # Extracting relevant data from the API response
    domain_name = data.get("hostname", domain)  # Ensure fallback value
    subdomains = data.get("subdomains", [])  # List of subdomains

    #extract A record
    a_records = data.get("current_dns",{}).get('a',{}).get("values",[])

    #extract for ip address
    ip_address = a_records[0] if a_records else "Unknown"

    #securityTrails doen't provide open ports
    ports_str, service_str = "{}", "{}"

    # Convert lists to PostgreSQL-compatible array format
    subdomains_str = "{" + ",".join(f'"{s}"' for s in subdomains) + "}" if subdomains else "{}"
    dns_records_str = "{" + ",".join(f'"{rec["ip"]}"' for rec in a_records) + "}" if a_records else "{}"

    db_configuration = {
        "dbname": "defaultdb",
        "user": "doadmin",
        "host": "***********",
        "port": "25060",
        "password": "************"
    }

    # Try connecting to the database
    try:
        with psycopg2.connect(**db_configuration) as conn:
            with conn.cursor() as cursor:
                # Insert data into the database
                cursor.execute(
                    """
                    INSERT INTO threat_data (ip_address, ports, services, domain_name, subdomains, dns_record)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """,
                    (str(ip_address), str(ports_str), str(services_str), str(domain_name), str(subdomains_str),
                     str(dns_records_str))
                )
                conn.commit()  # Commit the transaction
                print(f"Data for domain {domain_name} has been inserted successfully.")
    except Error as e:
        print(f"Database error: {e}")






DOMAIN = "umkc.edu"
API_KEY = "**************"
if __name__=="__main__":
    scan_domain(DOMAIN, API_KEY)

