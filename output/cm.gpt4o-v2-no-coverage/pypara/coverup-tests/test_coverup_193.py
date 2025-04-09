# file: pypara/monetary.py:555-582
# asked: {"lines": [569], "branches": [[566, 569]]}
# gained: {"lines": [569], "branches": [[566, 569]]}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.commons.errors import ProgrammingError
from pypara.currencies import Currency, CurrencyType
from pypara.exchange import FXRateLookupError, FXRateService
from pypara.monetary import SomeMoney, NoMoney

class MockFXRate:
    def __init__(self, value):
        self.value = value

class MockFXRateService:
    def __init__(self, rate=None, raise_attr_error=False):
        self.rate = rate
        self.raise_attr_error = raise_attr_error

    def query(self, ccy, to, asof, strict):
        if self.raise_attr_error:
            raise AttributeError("Mocked attribute error")
        return self.rate

@pytest.fixture
def mock_fxrate_service(monkeypatch):
    service = MockFXRateService()
    monkeypatch.setattr(FXRateService, 'default', service)
    return service

@pytest.fixture
def usd():
    return Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)

@pytest.fixture
def eur():
    return Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)

def test_convert_success(mock_fxrate_service, usd, eur):
    mock_fxrate_service.rate = MockFXRate(value=Decimal('1.25'))
    some_money = SomeMoney(usd, Decimal('100.00'), Date(2023, 1, 1))
    converted = some_money.convert(eur)
    assert converted.ccy == eur
    assert converted.qty == Decimal('125.00')
    assert converted.dov == Date(2023, 1, 1)

def test_convert_no_rate_strict(mock_fxrate_service, usd, eur):
    mock_fxrate_service.rate = None
    some_money = SomeMoney(usd, Decimal('100.00'), Date(2023, 1, 1))
    with pytest.raises(FXRateLookupError):
        some_money.convert(eur, strict=True)

def test_convert_no_rate_non_strict(mock_fxrate_service, usd, eur):
    mock_fxrate_service.rate = None
    some_money = SomeMoney(usd, Decimal('100.00'), Date(2023, 1, 1))
    converted = some_money.convert(eur, strict=False)
    assert converted == NoMoney

def test_convert_attribute_error(mock_fxrate_service, usd, eur):
    mock_fxrate_service.raise_attr_error = True
    some_money = SomeMoney(usd, Decimal('100.00'), Date(2023, 1, 1))
    with pytest.raises(AttributeError):
        some_money.convert(eur)

def test_convert_no_fxrate_service(mock_fxrate_service, monkeypatch, usd, eur):
    monkeypatch.setattr(FXRateService, 'default', None)
    some_money = SomeMoney(usd, Decimal('100.00'), Date(2023, 1, 1))
    with pytest.raises(ProgrammingError):
        some_money.convert(eur)
