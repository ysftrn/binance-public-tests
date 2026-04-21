import pytest
import requests

klines_url = "/api/v3/klines"


def test_klines(base_url):
    response = requests.get(f"{base_url}{klines_url}?symbol=BTCUSDT&interval=1m&limit=5")
    assert response.status_code == 200

def test_klines_response_time(base_url):
    res = requests.get(f"{base_url}{klines_url}?symbol=BTCUSDT&interval=1m&limit=5")

    assert res.elapsed.total_seconds() < 1.0

def test_data_types(base_url):
    res = requests.get(f"{base_url}{klines_url}?symbol=BTCUSDT&interval=1m&limit=5")
    data = res.json()
    assert isinstance(data, list)
    for item in data:
        assert isinstance(item, list)
        assert len(item) == 12
        assert isinstance(item[0], int)
        assert_is_string_floatable(item[1], "open")
        assert_is_string_floatable(item[2], "high")
        assert_is_string_floatable(item[3], "low")
        assert_is_string_floatable(item[4], "close")
        assert_is_string_floatable(item[5], "volume")

def assert_is_string_floatable(value, field_name):
    try:
        float(value)
    except ValueError:
        pytest.fail(f"{field_name} is not a floatable string: {value}")