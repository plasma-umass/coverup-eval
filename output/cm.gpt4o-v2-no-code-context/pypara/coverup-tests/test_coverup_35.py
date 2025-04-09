# file: pypara/monetary.py:1249-1276
# asked: {"lines": [1249, 1251, 1254, 1257, 1258, 1259, 1260, 1261, 1263, 1266, 1268, 1270, 1273, 1276], "branches": [[1260, 1261], [1260, 1263], [1266, 1268], [1266, 1276], [1268, 1270], [1268, 1273]]}
# gained: {"lines": [1249, 1251, 1254, 1257, 1258, 1259, 1260, 1261, 1266, 1268, 1270, 1273, 1276], "branches": [[1260, 1261], [1266, 1268], [1266, 1276], [1268, 1270], [1268, 1273]]}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import SomePrice, Currency, FXRateService, ProgrammingError, FXRateLookupError, NoPrice

class MockFXRate:
    def __init__(self, value):
        self.value = value

class MockFXRateService:
    def __init__(self, rate=None):
        self.rate = rate

    def query(self, from_ccy, to_ccy, asof, strict):
        return self.rate

@pytest.fixture
def mock_fx_rate_service(monkeypatch):
    service = MockFXRateService()
    monkeypatch.setattr(FXRateService, 'default', service)
    return service

@pytest.fixture
def mock_currency():
    return Currency('USD', 'US Dollar', 2, Decimal('0.01'), None, None)

def test_convert_success(mock_fx_rate_service, mock_currency):
    mock_fx_rate_service.rate = MockFXRate(Decimal('1.25'))
    price = SomePrice(mock_currency, Decimal('100.00'), Date(2023, 1, 1))
    converted_price = price.convert(Currency('EUR', 'Euro', 2, Decimal('0.01'), None, None))
    assert converted_price.ccy == Currency('EUR', 'Euro', 2, Decimal('0.01'), None, None)
    assert converted_price.qty == Decimal('125.00')
    assert converted_price.dov == Date(2023, 1, 1)

def test_convert_no_fx_rate_service(mock_currency):
    FXRateService.default = None
    price = SomePrice(mock_currency, Decimal('100.00'), Date(2023, 1, 1))
    with pytest.raises(ProgrammingError, match="Did you implement and set the default FX rate service?"):
        price.convert(Currency('EUR', 'Euro', 2, Decimal('0.01'), None, None))

def test_convert_fx_rate_lookup_error_strict(mock_fx_rate_service, mock_currency):
    mock_fx_rate_service.rate = None
    price = SomePrice(mock_currency, Decimal('100.00'), Date(2023, 1, 1))
    with pytest.raises(FXRateLookupError):
        price.convert(Currency('EUR', 'Euro', 2, Decimal('0.01'), None, None), strict=True)

def test_convert_fx_rate_lookup_error_non_strict(mock_fx_rate_service, mock_currency):
    mock_fx_rate_service.rate = None
    price = SomePrice(mock_currency, Decimal('100.00'), Date(2023, 1, 1))
    converted_price = price.convert(Currency('EUR', 'Euro', 2, Decimal('0.01'), None, None), strict=False)
    assert converted_price == NoPrice
