# file: pypara/monetary.py:1196-1202
# asked: {"lines": [1196, 1198, 1199, 1200, 1201, 1202], "branches": []}
# gained: {"lines": [1196, 1198, 1199, 1200, 1201, 1202], "branches": []}

import pytest
from decimal import Decimal, DivisionByZero, InvalidOperation
from pypara.monetary import SomePrice, NoPrice
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

@pytest.fixture
def usd_currency():
    return Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)

@pytest.fixture
def some_price(usd_currency):
    qty = Decimal("100.00")
    dov = Date(2023, 10, 1)
    return SomePrice(usd_currency, qty, dov)

def test_someprice_divide_valid(some_price, usd_currency):
    result = some_price.divide(2)
    assert result == SomePrice(usd_currency, Decimal("50.00"), some_price.dov)

def test_someprice_divide_invalid_operation(some_price):
    result = some_price.divide("invalid")
    assert result == NoPrice

def test_someprice_divide_division_by_zero(some_price):
    result = some_price.divide(0)
    assert result == NoPrice
