
import psycopg2
import Shodan
import SecurityTrails
import VirusTotal
from time import sleep
import requests

#details for the API
SHODAN_API_KEY = Shodan.API_KEY
SECURIT_TRAILS =  SecurityTrails.API_KEY
VIRUS_TOTAL = VirusTotal.API_KEY

#set the database connection details
DB_HOST = "localhost"
DB_NAME ="threat_intel"
DB_USER = 'admin'
DB_PASS = "securepass"


#integrating shodan
def fetch_data():
    response =Shodan.response
    return response

#integrating security trails
def security_data():
    response = SecurityTrails.response
    return response

def virus_data_fetch(domain):
    """Integrating virus_total to fetch data about the reputation of the domain and
    it is security status"""
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{domain}"
    header = VirusTotal.headers
    response =requests.get(url, headers=header)
    #checking if the response is successfull
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error in fetching data from virus total {response.status_code}")
        return

    #integrating it with the database
def store_threat_intelligence(threat_name, vulnerability, likelihood, impact):
    #fetching threat intelligence and storing them into the PostgreSQL database
    try:
        conn = psycopg2.connect(dbname=DB_NAME,
                                user=DB_USER,
                                password = DB_PASS,
                                host =DB_HOST )
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO tva_mapping(asset_id, threat_name,
vulnerability_description, likelihood, impact) VALUES
(%s, %s, %s, %s, %s)"""
        , (threat_name, vulnerability, likelihood, impact))
        conn.commit() #To finalize transaction the database
        cursor.close() #close the cursor from executing
        conn.close() #close the connection to database


    except  Exception as e:
        print(f"Error storing the data: {e}")

def Main():
    """The main function to store and fetch data periodically"""
    #domain and IP for demostration

    domain = SecurityTrails.DOMAIN
    # shodan fetching data
    shodan_data = fetch_data()
    if shodan_data:
        #retrieve exposed ports
        ports = shodan_data.get('ports', [])
        #dictionary to store the data
        store_threat_intelligence(threat_name="Exposed ports",
                                  vulnerability= f"Exposed ports {', '. join(map(str,ports))}",
        likelihood= 4,
        impact=5)

        #fetch data with virus total
        virus_data = virus_data_fetch( domain)
        if virus_data:
            if 'data' in virus_data:
                attributes = virus_data['data']['attributes']
                threat_score = attributes.get("reputation", 'N/A')
                store_threat_intelligence(threat_name="VirusTotal Domain Reputation",
                                          vulnerability=f"Domain reputation score: {threat_score}",
                                          likelihood=3,impact=4)

            #fetch dta with security trails
            security_trails_data=security_data()
            if security_trails_data:
                for record in security_trails_data.get('records', []):
                    store_threat_intelligence(threat_name="DNS Records",
                                              vulnerability=f"DNS record{record['record']}",
                                              likelihood=3,
                                              impact=4)



    if __name__ == "__main__":
        while True:
            Main()
            #scheduling it to runn periodically
            sleep(7200) #make it sleep for 2 hours after fetching data


