import pytest
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

if __name__ == "__main__":
    pytest.main()