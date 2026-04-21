import requests
import pytest

exchange_info_url = "/api/v3/exchangeInfo"
def test_exchange_info(base_url):
    response = requests.get(f"{base_url}{exchange_info_url}")
    assert response.status_code == 200

def test_exchange_info_response_time(base_url):
    res = requests.get(f"{base_url}{exchange_info_url}")
    assert res.elapsed.total_seconds() < 1.0


def test_exchange_info_data_types(base_url):
    res = requests.get(f"{base_url}{exchange_info_url}")
    data = res.json()
    assert isinstance(data, dict)
    assert "symbols" in data
    assert isinstance(data["symbols"], list)
    for item in data["symbols"]:
        assert isinstance(item, dict)
        assert "symbol" in item
        assert "status" in item
        assert "baseAsset" in item
        assert "baseAssetPrecision" in item
        assert "quoteAsset" in item
        assert "quotePrecision" in item
        assert "quoteAssetPrecision" in item
        assert "baseCommissionPrecision" in item
        assert "quoteCommissionPrecision" in item
        assert "quoteCommissionPrecision" in item
        assert "orderTypes" in item
        assert isinstance(item["orderTypes"], list)
        assert len(item["orderTypes"]) > 0


