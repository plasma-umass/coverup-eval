# file: pypara/exchange.py:130-163
# asked: {"lines": [130, 131, 136, 139, 141, 142, 152, 154, 155, 163], "branches": []}
# gained: {"lines": [130, 131, 136, 139, 141, 142, 154, 155], "branches": []}

import pytest
from pypara.exchange import FXRateService
from unittest.mock import MagicMock
from datetime import date

class MockFXRateService(FXRateService):
    def query(self, ccy1, ccy2, asof, strict=False):
        if ccy1 == "USD" and ccy2 == "EUR" and asof == date(2023, 1, 1):
            return 0.85
        if strict:
            raise LookupError("Rate not found")
        return None

    def queries(self, queries, strict=False):
        results = []
        for ccy1, ccy2, asof in queries:
            if ccy1 == "USD" and ccy2 == "EUR" and asof == date(2023, 1, 1):
                results.append(0.85)
            elif strict:
                raise LookupError("Rate not found")
            else:
                results.append(None)
        return results

@pytest.fixture
def fx_rate_service():
    return MockFXRateService()

def test_query_success(fx_rate_service):
    rate = fx_rate_service.query("USD", "EUR", date(2023, 1, 1))
    assert rate == 0.85

def test_query_failure_non_strict(fx_rate_service):
    rate = fx_rate_service.query("USD", "GBP", date(2023, 1, 1))
    assert rate is None

def test_query_failure_strict(fx_rate_service):
    with pytest.raises(LookupError):
        fx_rate_service.query("USD", "GBP", date(2023, 1, 1), strict=True)

def test_queries_success(fx_rate_service):
    queries = [("USD", "EUR", date(2023, 1, 1))]
    rates = list(fx_rate_service.queries(queries))
    assert rates == [0.85]

def test_queries_failure_non_strict(fx_rate_service):
    queries = [("USD", "GBP", date(2023, 1, 1))]
    rates = list(fx_rate_service.queries(queries))
    assert rates == [None]

def test_queries_failure_strict(fx_rate_service):
    queries = [("USD", "GBP", date(2023, 1, 1))]
    with pytest.raises(LookupError):
        list(fx_rate_service.queries(queries, strict=True))
