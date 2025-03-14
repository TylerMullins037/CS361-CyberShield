import schedule
import time
import SecurityTrails
from fetch_osint import fetch_data, store_threat_intelligence, security_data,virus_data_fetch

def run_osint_updates():
    try:
        data_available = fetch_data() #
        #iterate through fetched data
        for  data in data_available:
            threat_name = data.get('threat_name')
            vulnerability = data.get('vulnerability')
            likelihood = data.get('likelihood')
            impact = data.get('impact')
            #store them in the database
            store_threat_intelligence(threat_name,vulnerability, likelihood, impact)
            #information feteched by security trails
        security_trials_data = security_data()
        for data in security_trials_data:
            name = data.get('threat_name')
            vulnerability = data.get('vulnerability')
            likelihood = data.get('likelihood')
            impact = data.get('impact')
            store_threat_intelligence(name, vulnerability, likelihood, impact)

        domain = SecurityTrails.DOMAIN
        virus_data = virus_data_fetch(domain)
        if not virus_data:
            print(f"No virus found in this {domain} domain")
        for subdomain in virus_data:
            threat_name = subdomain.get("VirusTotalDomain", "Unknown threat")
            vulnerability = subdomain.get("Subdomain vulnerability", "unknown further investigation needed" )
            likelihood = subdomain.get("likelihood", "Medium" ) #likelihood
            impact = subdomain.get("impact", "High")  #impact
            #get the threat name
            print(f"The list name of the threat is {threat_name}")
            store_threat_intelligence(threat_name, vulnerability, likelihood, impact)

        print(f"successfully processed {len(virus_data)} threat intelligence data")

    except Exception as e:
        print(f'Error fetching the threat updates {e}')
# Schedule API calls every 6 hours
schedule.every(6).hours.do(run_osint_updates)
while True:
    schedule.run_pending()
    time.sleep(1)