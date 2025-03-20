import requests
from psycopg2 import Error
import psycopg2

API_KEY = "*****************"
IP = "8.8.8.8"  # You can also use a file hash instead of an IP
URL = f"https://www.virustotal.com/api/v3/ip_addresses/{IP}"

headers = {
    "x-apikey": API_KEY
}

response = requests.get(URL, headers=headers)

def scan_domain_virustotal(domain, api_key):
    """Scan domain using VirusTotal API and store results in PostgreSQL"""
    try:
        URL = f"https://www.virustotal.com/api/v3/domains/{domain}"

        headers = {
            "x-apikey": api_key
        }

        # API Request
        try:
            response = requests.get(URL, headers=headers)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f" API Request Error: {e}")
            return

        if response.status_code == 200:
            data = response.json()  # Parse the JSON response

            # Extracting Data
            attributes = data.get("data", {}).get("attributes", {})

            domain_name = attributes.get("id", domain)  # Domain name
            subdomains = attributes.get("subdomains", [])  # Subdomains
            dns_records = attributes.get("last_dns_records", [])  # DNS Records

            # look for ip address
            ip_address = attributes.get("last_analysis_results", {}).get("ip_address", "Unknown")

            # Look for open ports
            ports = attributes.get("network", {}).get("ports", [])
            services = attributes.get("categories", [])  #list of detected catagories

            #convert them for the SQL format
            subdomains_str = "{" + ",".join(f'"{s}"' for s in subdomains) + "}" if subdomains else "{}"
            dns_records_str = "{" + ",".join(f'"{d}"' for d in dns_records) + "}" if dns_records else "{}"
            ports_str = "{" + ",".join(map(str, ports)) + "}" if ports else "{}"
            services_str = "{" + ",".join(f'"{s}"' for s in services) + "}" if services else "{}"

            # configuring the database
            db_configuration = {
                "dbname": "defaultdb",
                "user": "doadmin",
                "host": "*********",
                "port": "25060",
                "password": "*********"
            }

            # insert information into the database
            try:
                with psycopg2.connect(**db_configuration) as conn:
                    with conn.cursor() as cursor:
                        cursor.execute(
                            """
                            INSERT INTO threat_data (ip_address, ports, services, domain_name, subdomains, dns_record)
                            VALUES (%s, %s, %s, %s, %s, %s)
                            """,
                            (ip_address[:45], ports_str, services_str, domain_name[:100], subdomains_str, dns_records_str)
                        )
                        conn.commit()  # Commit transaction
                        print(f"✅ Data for domain {domain_name} inserted successfully.")
            except Error as db_error:
                print(f"Database Error: {db_error}")

        else:
            print(f"API Error: {response.status_code}, Could not fetch data for domain {domain}")

    except Exception as e:
        print(f" General Error: {e}")

if __name__ == "__main__":
    domain = "jccc.edu"
    key = "*****************"
    scan_domain_virustotal(domain, key)
