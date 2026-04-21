# test_server_time.py
import requests

time_url = "/api/v3/time"

def test_server_time(base_url):
    response = requests.get(f"{base_url}{time_url}")
    data = response.json()
    assert response.status_code == 200
    assert "serverTime" in data
    assert isinstance(data["serverTime"], int)

def test_server_time_response_time(base_url):
    res = requests.get(f"{base_url}{time_url}")
    assert res.elapsed.total_seconds() < 1.0

