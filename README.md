# Binance Public API Test Suite

![thumbnail.png](thumbnail.png)
A pytest-based test suite for Binance's public REST API endpoints. Built as a QA portfolio project to demonstrate API testing fundamentals: response validation, data type assertions, response time testing, parametrized tests, and CI integration.

---

## Project Structure

```
binance-public-tests/
├── tests/~~~~
│   ├── conftest.py            # Shared fixtures (base_url)
│   ├── test_ping.py
│   ├── test_server_time.py
│   ├── test_exchange_info.py
│   ├── test_depth.py
│   ├── test_book_depth.py
│   ├── test_klines.py
│   └── test_ticker_price.py
└── .github/
    └── workflows/
        └── tests.yml
```

Each file covers a single endpoint and contains all relevant tests for that endpoint: status code, response time, response structure, and data type validation.

---

## Endpoints Tested

| File | Endpoint | Description |
|---|---|---|
| `test_ping.py` | `/api/v3/ping` | Connectivity check |
| `test_server_time.py` | `/api/v3/time` | Server timestamp |
| `test_exchange_info.py` | `/api/v3/exchangeInfo` | Symbol and market metadata |
| `test_depth.py` | `/api/v3/depth` | Order book (bids/asks) |
| `test_book_depth.py` | `/api/v3/ticker/bookTicker` | Best bid/ask per symbol |
| `test_klines.py` | `/api/v3/klines` | Candlestick (OHLCV) data |
| `test_ticker_price.py` | `/api/v3/ticker/price` | Latest price per symbol |

---

## Test Types

**Status code validation** — every endpoint is checked for the expected HTTP response code, including negative cases (invalid symbols, missing parameters).

**Response time assertions** — every endpoint must respond within 1 second, measured using `requests`' built-in `elapsed` attribute rather than manual timers.

**Response structure validation** — required fields are asserted to be present and of the correct type (e.g. `serverTime` must be an `int`, price fields must be `str`).

**Numeric string validation** — price and quantity fields arrive as strings for floating point precision reasons. A helper function `assert_is_float_string()` verifies these can be converted to `float` without errors.

**Parametrized tests** — `pytest.mark.parametrize` is used to run the same test logic against multiple inputs (e.g. valid symbols, invalid symbols) without duplicating test functions.

---

## Design Decisions

**One file per endpoint** — all tests for a given endpoint live in a single file. This makes it easy to find, read, and extend tests without jumping between files.

**Testing what matters** — tests assert fields that a consuming application would actually depend on, rather than exhaustively checking every field in the response. For example, in `exchangeInfo`, fields like `symbol`, `baseAsset`, `quoteAsset`, and `orderTypes` are validated because a trading bot depends on them. Fields like `timezone` are not tested because their absence would not break anything.

**No connection reuse** — each test makes an independent HTTP request. Sharing connections between tests would introduce state and coupling, which violates test isolation principles.

**`elapsed` over `time.time()`** — `requests.Response.elapsed` measures only the round-trip time of the HTTP request itself, excluding Python overhead. This gives a cleaner and more accurate response time measurement.

---

## Running the Tests

**Requirements:**
- Python 3.11
- pytest
- requests

**Install dependencies:**
```bash
pip install pytest requests
```

**Run all tests:**
```bash
pytest tests/ -v
```

**Run a single file:**
```bash
pytest tests/test_depth.py -v
```

---

## CI Note

A GitHub Actions workflow is configured to run on every push. However, the pipeline currently fails with HTTP 451 (Unavailable For Legal Reasons) because Binance blocks requests from US-based IP addresses, which is where GitHub Actions runners are hosted. This is a geographic restriction on Binance's side, not a code issue.

All 23 tests pass when run locally from a non-restricted location.
