import requests
import psycopg2
from psycopg2 import Error

def scan_domain(domain, api_key):
    #Scanning the domain for vulnerabilities and storing them in the PostgreSQL database
    try:
        URL = f"https://api.securitytrails.com/v1/domain/{domain}"

        headers = {
            "APIKEY": api_key
        }

        # Try the API request
        try:
            response = requests.get(URL, headers=headers)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"API request error: {e}")
            return

        if response.status_code == 200:
            data = response.json()  # Parse the JSON response

            # Extracting relevant data from the API response
            domain_name = data.get("hostname", domain)  # Ensure fallback value
            subdomains = data.get("subdomains", [])  # List of subdomains

            #extract A record
            a_records = data.get("current_dns",{}).get('a',{}).get("values",[])

            #extract for ip address
            ip_address = a_records[0] if a_records else "Unknown"
            #fetch for open ports
            ports = data.get("ports", [])   #ports like 80, 443
            services = data.get("services", []) #get https or http

            # Convert lists to PostgreSQL-compatible array format
            subdomains_str = "{" + ",".join(f'"{s}"' for s in subdomains) + "}" if subdomains else "{}"
            dns_records_str = "{" + ",".join(f'"{rec["ip"]}"' for rec in a_records) + "}" if a_records else "{}"

            #security trails is not providing ports and services
            ports_str =  "{}"
            services_str =  "{}"

            #Ensuring atleast one IP is available
            if ip_address is None:
                ip_address = "unknown"

            db_configuration = {
                "dbname": "defaultdb",
                "user": "doadmin",
                "host": "**********",
                "port": "25060",
                "password": "********"
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

        else:
            print(f"API error: {response.status_code}, Could not fetch data for domain {domain}")

    except Exception as e:
        print(f"General error: {e}")




DOMAIN = "umkc.edu"
API_KEY = "**********"
if __name__=="__main__":
    scan_domain(DOMAIN, API_KEY)
    #domain = "google.com"
    api_key = "***********"
