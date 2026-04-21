# test_ping.py
import requests


ping_url = "/api/v3/ping"


def test_ping(base_url):
    response = requests.get(f"{base_url}{ping_url}")
    assert response.status_code == 200

def test_ping_response_time(base_url):
    res = requests.get(f"{base_url}{ping_url}")
    assert res.elapsed.total_seconds() < 1.0