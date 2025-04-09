# file: pypara/monetary.py:1249-1276
# asked: {"lines": [1251, 1254, 1257, 1258, 1259, 1260, 1261, 1263, 1266, 1268, 1270, 1273, 1276], "branches": [[1260, 1261], [1260, 1263], [1266, 1268], [1266, 1276], [1268, 1270], [1268, 1273]]}
# gained: {"lines": [1251, 1254, 1257, 1258, 1259, 1260, 1261, 1266, 1268, 1270, 1273, 1276], "branches": [[1260, 1261], [1266, 1268], [1266, 1276], [1268, 1270], [1268, 1273]]}

import pytest
from decimal import Decimal
from pypara.commons.errors import ProgrammingError
from pypara.commons.zeitgeist import Date
from pypara.currencies import Currency, CurrencyType
from pypara.exchange import FXRateLookupError, FXRateService
from pypara.monetary import SomePrice, NoPrice

class MockFXRate:
    def __init__(self, value):
        self.value = value

class MockFXRateService(FXRateService):
    def query(self, ccy1, ccy2, asof, strict=False):
        if ccy1.code == "USD" and ccy2.code == "EUR":
            return MockFXRate(Decimal("0.85"))
        return None

    def queries(self, queries, strict=False):
        return [self.query(ccy1, ccy2, asof, strict) for ccy1, ccy2, asof in queries]

@pytest.fixture
def mock_fx_rate_service(monkeypatch):
    service = MockFXRateService()
    monkeypatch.setattr(FXRateService, 'default', service)
    return service

@pytest.fixture
def currencies():
    usd = Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY)
    eur = Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)
    jpy = Currency.of("JPY", "Japanese Yen", 0, CurrencyType.MONEY)
    return usd, eur, jpy

def test_convert_success(mock_fx_rate_service, currencies):
    usd, eur, _ = currencies
    price = SomePrice(usd, Decimal("100"), Date(2023, 1, 1))
    converted = price.convert(eur)
    assert converted.ccy == eur
    assert converted.qty == Decimal("85.00")
    assert converted.dov == Date(2023, 1, 1)

def test_convert_no_rate_strict(mock_fx_rate_service, currencies):
    usd, _, jpy = currencies
    price = SomePrice(usd, Decimal("100"), Date(2023, 1, 1))
    with pytest.raises(FXRateLookupError):
        price.convert(jpy, strict=True)

def test_convert_no_rate_non_strict(mock_fx_rate_service, currencies):
    usd, _, jpy = currencies
    price = SomePrice(usd, Decimal("100"), Date(2023, 1, 1))
    converted = price.convert(jpy, strict=False)
    assert converted == NoPrice

def test_convert_no_fx_service(monkeypatch, currencies):
    usd, eur, _ = currencies
    monkeypatch.setattr(FXRateService, 'default', None)
    price = SomePrice(usd, Decimal("100"), Date(2023, 1, 1))
    with pytest.raises(ProgrammingError):
        price.convert(eur)
