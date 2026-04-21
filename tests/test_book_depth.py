# test_book_depth.py
import requests
import pytest

book_ticker_url = "/api/v3/ticker/bookTicker"


def test_book_depth(base_url):
    response = requests.get(f"{base_url}{book_ticker_url}")
    assert response.status_code == 200

def test_book_depth_response_time(base_url):
    res = requests.get(f"{base_url}{book_ticker_url}")
    assert res.elapsed.total_seconds() < 1.0

def test_data_types(base_url):
    res = requests.get(f"{base_url}{book_ticker_url}")
    data = res.json()
    assert isinstance(data, list)
    for item in data:
        assert isinstance(item, dict)
        assert isinstance(item["symbol"], str)
        assert isinstance(item["bidPrice"], str)
        assert_is_string_floatable(item["bidPrice"], "bidPrice")
        assert isinstance(item["bidQty"], str)
        assert_is_string_floatable(item["bidQty"], "bidQty")
        assert isinstance(item["askPrice"], str)
        assert_is_string_floatable(item["askPrice"], "askPrice")
        assert isinstance(item["askQty"], str)
        assert_is_string_floatable(item["askQty"], "askQty")


def assert_is_string_floatable(value, field_name):
    try:
        float(value)
    except ValueError:
        pytest.fail(f"{field_name} is not a floatable string: {value}")