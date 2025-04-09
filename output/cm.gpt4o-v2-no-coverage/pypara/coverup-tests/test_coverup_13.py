# file: pypara/exchange.py:130-163
# asked: {"lines": [130, 131, 136, 139, 141, 142, 152, 154, 155, 163], "branches": []}
# gained: {"lines": [130, 131, 136, 139, 141, 142, 154, 155], "branches": []}

import pytest
from unittest.mock import Mock
from pypara.commons.zeitgeist import Date
from pypara.currencies import Currency
from pypara.exchange import FXRateService

class TestFXRateService(FXRateService):
    def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False):
        if ccy1 == ccy2:
            return 1.0
        if strict:
            raise LookupError("Rate not found")
        return None

    def queries(self, queries, strict: bool = False):
        results = []
        for ccy1, ccy2, asof in queries:
            results.append(self.query(ccy1, ccy2, asof, strict))
        return results

@pytest.fixture
def fx_service():
    return TestFXRateService()

def test_query_same_currency(fx_service):
    ccy = Mock(spec=Currency)
    date = Mock(spec=Date)
    assert fx_service.query(ccy, ccy, date) == 1.0

def test_query_different_currency_non_strict(fx_service):
    ccy1 = Mock(spec=Currency)
    ccy2 = Mock(spec=Currency)
    date = Mock(spec=Date)
    assert fx_service.query(ccy1, ccy2, date) is None

def test_query_different_currency_strict(fx_service):
    ccy1 = Mock(spec=Currency)
    ccy2 = Mock(spec=Currency)
    date = Mock(spec=Date)
    with pytest.raises(LookupError):
        fx_service.query(ccy1, ccy2, date, strict=True)

def test_queries(fx_service):
    ccy1 = Mock(spec=Currency)
    ccy2 = Mock(spec=Currency)
    date = Mock(spec=Date)
    queries = [(ccy1, ccy2, date), (ccy1, ccy1, date)]
    results = fx_service.queries(queries)
    assert results == [None, 1.0]
