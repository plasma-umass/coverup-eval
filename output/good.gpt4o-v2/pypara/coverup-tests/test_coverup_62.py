# file: pypara/monetary.py:1249-1276
# asked: {"lines": [1249, 1251, 1254, 1257, 1258, 1259, 1260, 1261, 1263, 1266, 1268, 1270, 1273, 1276], "branches": [[1260, 1261], [1260, 1263], [1266, 1268], [1266, 1276], [1268, 1270], [1268, 1273]]}
# gained: {"lines": [1249, 1251, 1254, 1257, 1258, 1259, 1260, 1261, 1263, 1266, 1268, 1270, 1273, 1276], "branches": [[1260, 1261], [1260, 1263], [1266, 1268], [1266, 1276], [1268, 1270], [1268, 1273]]}

import pytest
from decimal import Decimal
from pypara.commons.zeitgeist import Date
from pypara.currencies import Currency, CurrencyType
from pypara.exchange import FXRateService, FXRateLookupError
from pypara.commons.errors import ProgrammingError
from pypara.monetary import SomePrice, NoPrice

class MockFXRateService(FXRateService):
    def query(self, ccy1, ccy2, asof, strict=False):
        if ccy1 == Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY) and ccy2 == Currency.of("EUR", "Euro", 2, CurrencyType.MONEY):
            return MockFXRate(Decimal("0.85"))
        return None

    def queries(self, queries, strict=False):
        return [self.query(ccy1, ccy2, asof, strict) for ccy1, ccy2, asof in queries]

class MockFXRate:
    def __init__(self, value):
        self.value = value

@pytest.fixture
def mock_fx_rate_service(monkeypatch):
    service = MockFXRateService()
    monkeypatch.setattr(FXRateService, 'default', service)
    return service

def test_convert_success(mock_fx_rate_service):
    price = SomePrice(Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY), Decimal("100.00"), Date(2023, 1, 1))
    converted_price = price.convert(Currency.of("EUR", "Euro", 2, CurrencyType.MONEY))
    assert converted_price.ccy == Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)
    assert converted_price.qty == Decimal("85.00")
    assert converted_price.dov == Date(2023, 1, 1)

def test_convert_no_rate_strict(mock_fx_rate_service):
    price = SomePrice(Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY), Decimal("100.00"), Date(2023, 1, 1))
    with pytest.raises(FXRateLookupError):
        price.convert(Currency.of("GBP", "British Pound", 2, CurrencyType.MONEY), strict=True)

def test_convert_no_rate_non_strict(mock_fx_rate_service):
    price = SomePrice(Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY), Decimal("100.00"), Date(2023, 1, 1))
    converted_price = price.convert(Currency.of("GBP", "British Pound", 2, CurrencyType.MONEY), strict=False)
    assert converted_price == NoPrice

def test_convert_no_fx_service(monkeypatch):
    monkeypatch.setattr(FXRateService, 'default', None)
    price = SomePrice(Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY), Decimal("100.00"), Date(2023, 1, 1))
    with pytest.raises(ProgrammingError):
        price.convert(Currency.of("EUR", "Euro", 2, CurrencyType.MONEY))

def test_convert_attribute_error(monkeypatch):
    class FaultyFXRateService:
        def query(self, ccy1, ccy2, asof, strict=False):
            raise AttributeError("Some random attribute error")

        def queries(self, queries, strict=False):
            raise AttributeError("Some random attribute error")

    monkeypatch.setattr(FXRateService, 'default', FaultyFXRateService())
    price = SomePrice(Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY), Decimal("100.00"), Date(2023, 1, 1))
    with pytest.raises(AttributeError):
        price.convert(Currency.of("EUR", "Euro", 2, CurrencyType.MONEY))
