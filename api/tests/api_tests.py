import pytest
from api.virustotal_integration import scan_domain_virustotal
from api.shodan_integration import fetch_shodan_data

def test_shodan_api():
    # Fetch data for a known public IP (Google DNS)
    data = fetch_shodan_data("8.8.8.8")
    
    # Validate response structure
    assert isinstance(data, dict), "Response should be a dictionary"
    assert "ports" in data, "Response should contain 'ports' key"
    assert isinstance(data["ports"], list), "'ports' should be a list"
    
    # Validate that ports list is not empty
    assert len(data["ports"]) > 0, "Ports list should not be empty"

def test_virustotal_api():
    # Fetch data for a known domain (jccc.edu)
    data = scan_domain_virustotal("jccc.edu", "test_api_key")
    
    # Validate response structure (assuming scan_domain_virustotal returns a dictionary)
    assert isinstance(data, dict), "Response should be a dictionary"
    
    # Validate that key 'ip_address' exists in the response
    assert "ip_address" in data, "Response should contain 'ip_address' key"
    assert isinstance(data["ip_address"], str), "'ip_address' should be a string"
    
    # Validate that the 'ip_address' is not 'Unknown'
    assert data["ip_address"] != "Unknown", "IP address should not be 'Unknown'"
    
    # Validate that the 'ports' key exists and is a list
    assert "ports" in data, "Response should contain 'ports' key"
    assert isinstance(data["ports"], list), "'ports' should be a list"
    
    # Validate that ports list is not empty
    assert len(data["ports"]) > 0, "Ports list should not be empty"
    
    # Validate that the 'services' key exists and is a list
    assert "services" in data, "Response should contain 'services' key"
    assert isinstance(data["services"], list), "'services' should be a list"
    
    # Validate that services list is not empty
    assert len(data["services"]) > 0, "Services list should not be empty"
    
    # Check if the services list contains expected values
    expected_services = ["BitDefender", "Xcitium Verdict Cloud", "Sophos", "Forcepoint ThreatSeeker"]
    assert all(service in data["services"] for service in expected_services), "Not all expected services are in the response"



if __name__ == "__main__":
    pytest.main()
