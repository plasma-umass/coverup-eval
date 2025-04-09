# file: pypara/monetary.py:1249-1276
# asked: {"lines": [1263], "branches": [[1260, 1263]]}
# gained: {"lines": [1263], "branches": [[1260, 1263]]}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import SomePrice, Currency, FXRateService, ProgrammingError, FXRateLookupError, NoPrice

class MockFXRateService:
    def query(self, from_ccy, to_ccy, asof, strict):
        raise AttributeError("Mocked exception")

@pytest.fixture
def mock_fx_rate_service(monkeypatch):
    service = MockFXRateService()
    monkeypatch.setattr(FXRateService, 'default', service)
    return service

@pytest.fixture
def mock_currency():
    return Currency('USD', 'US Dollar', 2, 'USD', Decimal('0.01'), None)

def test_someprice_convert_attribute_error_with_default_none(mock_fx_rate_service, mock_currency):
    FXRateService.default = None
    some_price = SomePrice(mock_currency, Decimal('100.0'), Date(2023, 1, 1))
    
    with pytest.raises(ProgrammingError, match="Did you implement and set the default FX rate service?"):
        some_price.convert(Currency('EUR', 'Euro', 2, 'EUR', Decimal('0.01'), None))

def test_someprice_convert_attribute_error_with_default_set(mock_fx_rate_service, mock_currency):
    some_price = SomePrice(mock_currency, Decimal('100.0'), Date(2023, 1, 1))
    
    with pytest.raises(AttributeError, match="Mocked exception"):
        some_price.convert(Currency('EUR', 'Euro', 2, 'EUR', Decimal('0.01'), None))
