import pytest
from api.shodan_integration import fetch_shodan_data
def test_shodan_api():
data = fetch_shodan_data("8.8.8.8")
assert "ports" in data
assert isinstance(data["ports"], list)
pytest.main()
