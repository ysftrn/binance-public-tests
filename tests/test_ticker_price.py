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

