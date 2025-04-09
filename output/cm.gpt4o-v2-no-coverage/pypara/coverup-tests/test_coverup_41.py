# file: pypara/monetary.py:1164-1180
# asked: {"lines": [1164, 1165, 1166, 1174, 1175, 1177, 1178, 1180], "branches": [[1165, 1166], [1165, 1168], [1177, 1178], [1177, 1180]]}
# gained: {"lines": [1164, 1165, 1166, 1174, 1175, 1177, 1178, 1180], "branches": [[1165, 1166], [1165, 1168], [1177, 1178], [1177, 1180]]}

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice, IncompatibleCurrencyError
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

class MockPrice:
    def __init__(self, ccy, qty, dov, undefined=False):
        self.ccy = ccy
        self.qty = qty
        self.dov = dov
        self.undefined = undefined

    def __iter__(self):
        return iter((self.ccy, self.qty, self.dov))

@pytest.fixture
def usd_currency():
    return Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)

@pytest.fixture
def eur_currency():
    return Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)

@pytest.fixture
def some_price_usd(usd_currency):
    return SomePrice(usd_currency, Decimal("100.00"), Date(2023, 1, 1))

@pytest.fixture
def some_price_usd_50(usd_currency):
    return SomePrice(usd_currency, Decimal("50.00"), Date(2023, 1, 2))

@pytest.fixture
def some_price_eur(eur_currency):
    return SomePrice(eur_currency, Decimal("100.00"), Date(2023, 1, 1))

def test_subtract_undefined(some_price_usd):
    other = MockPrice(None, None, None, undefined=True)
    result = some_price_usd.subtract(other)
    assert result == some_price_usd

def test_subtract_different_currency(some_price_usd, some_price_eur):
    with pytest.raises(IncompatibleCurrencyError):
        some_price_usd.subtract(some_price_eur)

def test_subtract_same_currency(some_price_usd, some_price_usd_50):
    result = some_price_usd.subtract(some_price_usd_50)
    assert result.ccy == some_price_usd.ccy
    assert result.qty == Decimal("50.00")
    assert result.dov == some_price_usd_50.dov
