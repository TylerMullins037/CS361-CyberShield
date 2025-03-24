import requests
import psycopg2
from risk_prioritization import RiskPrioritizationModel, determine_base_risk,determine_likelihood

API_KEY = "***********"
IP = "8.8.8.8"
def shodan_integration(ip_address, api_key, model, active_incidents=None, asset_value=None):
    try:
        URL = f"https://api.shodan.io/shodan/host/{IP}?key={API_KEY}"

        try:
            response = requests.get(URL)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Shodan API Request Error: {e}")
            return
        if response.status_code == 200:
            #parse as json response
            data = response.json()

            #check for open ports and services
            ports = data.get("ports", [])  # List of open ports
            services = extract_service(data)

            #determine threat_level from shodan
            threat_type = determine_threat_type(data)

            #Determine other factors based on prioritization model
            base_risk, impact = determine_base_risk(ports, services)
            likelihood = determine_likelihood(ports)
            # Dynamically adjust time_sensitivity based on real-time factors
            time_sensitivity = adjust_time_sensitivity(active_incidents, threat_type)

            # Dynamically adjust asset_value based on the criticality of the asset
            asset_value = adjust_asset_value(asset_value)

            # Create a threat dictionary for prioritization
            threat_data = {
                "ip_address": IP,
                "base_risk": base_risk,
                "impact": impact,
                "likelihood": likelihood,
                "time_sensitivity": time_sensitivity,
                "asset_value": asset_value,
                "threat_type": threat_type
            }

            # Use the model to calculate the score for the threat
            threat_score = model.calculate_score(threat_data)
            threat_data["score"] = threat_score

            # Store the data in the PostgreSQL database
            store_in_database(IP, ports, services, threat_type, threat_score)
    except Exception as e:
        print(f"Error: {e}")
def store_in_database(IP, ports, services, threat_type, threat_score):
    try:
        #Store the data in the database
        conn = psycopg2.connect(dbname="defaultdb",
                            user = "doadmin",
                            host="**************",
                            port="25060",
                            password="***********"
        )
        cursor = conn.cursor()
        ports_str = "{" + ",".join(map(str, ports)) + "}" if ports else "{}"
        services_str = "{" + ",".join(f'"{s}"' for s in services) + "}" if services else "{}"
        cursor.execute(
           "INSERT INTO threat_data (ip_address, ports, services, threat_type, threat_score) VALUES (%s, %s, %s, %s,%s)",
        ((IP, ports_str, services_str, threat_type, threat_score) ))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Data for IP {IP} successfully stored in the database.")
    except Exception as e:
        print(f"Error {e}")
def extract_service(data):
    """Extracts service names from shodan"""
    service = set()
    for item in data.get("data", []):  # Iterate through service data
        service_name = item.get("product", "Unknown")
        if service_name != "Unknown":
            service.add(service_name)

    return list(service) if service else ["Unknown"]
def adjust_asset_value(asset_importance):
    """Adjust asset value based on the importance of the asset being threatened"""
    if asset_importance == "critical":
        return 10  # Critical assets should have the highest value
    elif asset_importance == "high":
        return 7  # High-value assets
    elif asset_importance == "medium":
        return 5  # Medium-value assets
    return 3  # Low-value or non-critical assets
def adjust_time_sensitivity(active_incidents, threat_type):
    """Adjust time_sensitivity dynamically based on active incidents or threat type"""
    # If there are active incidents and the threat type is related to something urgent, increase time_sensitivity
    if active_incidents:
        for incident in active_incidents:
            if incident in ["DDoS", "Malware","Ransomware", "SQL Injection"]:
                return 10  # Urgent time sensitivity for certain types of incidents
    if threat_type == "High Risk - Malicious Activity Detected":
        return 8  # High risk might indicate the need for faster action
    return 5  # Default time_sensitivity
def determine_threat_type(data):
    """Determine threat levels"""
    if "tags" in data and "malicious" in data["tags"]:
        return "High Risk - Malicious Activity Detected"
    elif len(data.get("ports", [])) > 5:
        return "Medium Risk - Multiple Open Ports"
    elif len(data.get("ports", [])) > 0:
        return "Low Risk - Open Ports Detected"
    else:
        return "No Risk - No Open Ports"
model = RiskPrioritizationModel()
active= ['DDOS', 'Malware', 'Ransomware','SQL Injection']
assets_value = "critical"
threats = shodan_integration(IP,API_KEY, model, active, assets_value)
if threats:
    #using model to prioritize risks
    prioritize = model.prioritize_threats([threats])
    # Print the prioritized threats
    print("Prioritized Threats:")
    for threat in prioritize:
        print(f"{threat['ip_address']} - Risk Score: {threat['risk_score']}")

    # Get critical threats above a certain threshold  of 70
    critical_threats = model.get_critical_threats(prioritize, threshold=0.70)
    print("\nCritical Threats (Risk Score >= 0.70):")
    for threat in critical_threats:
        print(f"{threat['ip_address']} - Risk Score: {threat['risk_score']}")
