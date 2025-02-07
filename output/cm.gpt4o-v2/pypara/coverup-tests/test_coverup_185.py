# file: pypara/monetary.py:555-582
# asked: {"lines": [569], "branches": [[566, 569]]}
# gained: {"lines": [569], "branches": [[566, 569]]}

import pytest
from decimal import Decimal
from pypara.commons.errors import ProgrammingError
from pypara.commons.zeitgeist import Date
from pypara.currencies import Currency, CurrencyType
from pypara.exchange import FXRateLookupError, FXRateService
from pypara.monetary import SomeMoney, NoMoney

def test_convert_fx_rate_service_default_none(monkeypatch):
    # Setup
    ccy = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    to = Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)
    qty = Decimal("100.00")
    dov = Date(2023, 1, 1)
    some_money = SomeMoney(ccy, qty, dov)

    # Mock FXRateService.default to be None
    monkeypatch.setattr(FXRateService, "default", None)

    # Test and Assert
    with pytest.raises(ProgrammingError, match="Did you implement and set the default FX rate service?"):
        some_money.convert(to)

def test_convert_fx_rate_service_default_attribute_error(monkeypatch):
    # Setup
    ccy = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    to = Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)
    qty = Decimal("100.00")
    dov = Date(2023, 1, 1)
    some_money = SomeMoney(ccy, qty, dov)

    class MockFXRateService:
        def query(self, ccy, to, asof, strict):
            raise AttributeError("Mocked attribute error")

    # Mock FXRateService.default to raise AttributeError
    monkeypatch.setattr(FXRateService, "default", MockFXRateService())

    # Test and Assert
    with pytest.raises(AttributeError, match="Mocked attribute error"):
        some_money.convert(to)
