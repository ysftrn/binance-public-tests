import requests
import pytest


ticker_price_url = "/api/v3/ticker/price"

def test_no_symbol(base_url):
    response = requests.get(f"{base_url}{ticker_price_url}")
    data = response.json()
    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0
    for item in data:
        assert isinstance (item, dict)
        assert isinstance(item["symbol"], str)
        assert isinstance(item["price"], str)


@pytest.mark.parametrize("symbol,expected_status", [
    ("BTCUSDT", 200),
    ("ETHUSDC", 200),
    ("INVALID", 400),
])
def test_ticker_validation(base_url, symbol, expected_status):
    res = requests.get(f"{base_url}{ticker_price_url}?symbol={symbol}")
    assert res.status_code == expected_status

def test_ticker_response_time(base_url):
    res = requests.get(f"{base_url}{ticker_price_url}")
    assert res.elapsed.total_seconds() < 1.0


@pytest.mark.parametrize("symbol", [
    ("BTCUSDT"),
    ("ETHUSDC")
])
def test_data_types_for_given_symbol(base_url, symbol):
    res = requests.get(f"{base_url}{ticker_price_url}?symbol={symbol}")
    data = res.json()
    assert isinstance(data, dict)
    assert isinstance(data["symbol"], str)
    assert isinstance(data["price"], str)
    assert_is_string_floatable(data["price"], "price")


def assert_is_string_floatable(value, field_name):
    try:
        float(value)
    except ValueError:
        pytest.fail(f"{field_name} is not a floatable string: {value}")
