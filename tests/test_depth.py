import requests
import pytest

depth_url = "/api/v3/depth"


def test_depth(base_url):
    response = requests.get(f"{base_url}{depth_url}?symbol=BTCUSDT")
    assert response.status_code == 200

def test_depth_response_time(base_url):
    res = requests.get(f"{base_url}{depth_url}?symbol=BTCUSDT")
    assert res.elapsed.total_seconds() < 1.0

def test_data_types(base_url):
    res = requests.get(f"{base_url}{depth_url}?symbol=BTCUSDT")
    data = res.json()
    assert isinstance(data, dict)
    assert "lastUpdateId" in data
    assert isinstance(data["lastUpdateId"], int)
    assert "bids" in data
    assert isinstance(data["bids"], list)
    assert "asks" in data
    assert isinstance(data["asks"], list)
    assert len(data["bids"]) > 0
    assert len(data["asks"]) > 0
    for item in data["bids"]:
        assert isinstance(item, list)
        assert len(item) == 2
        assert_is_string_floatable(item[0], "price")
        assert_is_string_floatable(item[1], "qty")

    for item in data["asks"]:
        assert isinstance(item, list)
        assert len(item) == 2
        assert_is_string_floatable(item[0], "price")
        assert_is_string_floatable(item[1], "qty")



def assert_is_string_floatable(value, field_name):
    try:
        float(value)
    except ValueError:
        pytest.fail(f"{field_name} is not a floatable string: {value}")
