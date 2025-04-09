# file: pypara/monetary.py:555-582
# asked: {"lines": [555, 557, 560, 563, 564, 565, 566, 567, 569, 572, 574, 576, 579, 582], "branches": [[566, 567], [566, 569], [572, 574], [572, 582], [574, 576], [574, 579]]}
# gained: {"lines": [555, 557, 560, 563, 564, 565, 566, 567, 569, 572, 574, 576, 579, 582], "branches": [[566, 567], [566, 569], [572, 574], [572, 582], [574, 576], [574, 579]]}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import SomeMoney, Currency, FXRateService, Money, NoMoney, ProgrammingError, FXRateLookupError

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
def usd_currency():
    return Currency('USD', 'US Dollar', 2, 'USD', Decimal('0.01'), None)

@pytest.fixture
def eur_currency():
    return Currency('EUR', 'Euro', 2, 'EUR', Decimal('0.01'), None)

def test_convert_success(mock_fx_rate_service, usd_currency, eur_currency):
    mock_fx_rate_service.rate = type('Rate', (object,), {'value': Decimal('1.25')})()
    some_money = SomeMoney(usd_currency, Decimal('100.00'), Date(2023, 1, 1))
    converted_money = some_money.convert(eur_currency)
    assert converted_money.ccy == eur_currency
    assert converted_money.qty == Decimal('125.00')
    assert converted_money.dov == Date(2023, 1, 1)

def test_convert_no_rate_strict(mock_fx_rate_service, usd_currency, eur_currency):
    mock_fx_rate_service.rate = None
    some_money = SomeMoney(usd_currency, Decimal('100.00'), Date(2023, 1, 1))
    with pytest.raises(FXRateLookupError):
        some_money.convert(eur_currency, strict=True)

def test_convert_no_rate_non_strict(mock_fx_rate_service, usd_currency, eur_currency):
    mock_fx_rate_service.rate = None
    some_money = SomeMoney(usd_currency, Decimal('100.00'), Date(2023, 1, 1))
    converted_money = some_money.convert(eur_currency, strict=False)
    assert converted_money == NoMoney

def test_convert_fx_service_not_set(monkeypatch, usd_currency, eur_currency):
    monkeypatch.setattr(FXRateService, 'default', None)
    some_money = SomeMoney(usd_currency, Decimal('100.00'), Date(2023, 1, 1))
    with pytest.raises(ProgrammingError):
        some_money.convert(eur_currency)

def test_convert_fx_service_attribute_error(monkeypatch, usd_currency, eur_currency):
    class FaultyFXRateService:
        def query(self, from_ccy, to_ccy, asof, strict):
            raise AttributeError("Some error")

    monkeypatch.setattr(FXRateService, 'default', FaultyFXRateService())
    some_money = SomeMoney(usd_currency, Decimal('100.00'), Date(2023, 1, 1))
    with pytest.raises(AttributeError):
        some_money.convert(eur_currency)
