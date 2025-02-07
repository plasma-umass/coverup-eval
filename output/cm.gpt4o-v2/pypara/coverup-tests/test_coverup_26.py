# file: pypara/monetary.py:1204-1210
# asked: {"lines": [1204, 1206, 1207, 1208, 1209, 1210], "branches": []}
# gained: {"lines": [1204, 1206, 1207, 1208, 1209, 1210], "branches": []}

import pytest
from decimal import Decimal, DivisionByZero, InvalidOperation
from pypara.monetary import SomePrice, NoPrice
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

@pytest.fixture
def usd_currency():
    return Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)

def test_floor_divide_valid(usd_currency):
    price = SomePrice(usd_currency, Decimal('100.00'), Date(2023, 10, 1))
    result = price.floor_divide(2)
    assert result == SomePrice(usd_currency, Decimal('50'), Date(2023, 10, 1))

def test_floor_divide_invalid_operation(usd_currency):
    price = SomePrice(usd_currency, Decimal('100.00'), Date(2023, 10, 1))
    result = price.floor_divide('invalid')
    assert result == NoPrice

def test_floor_divide_division_by_zero(usd_currency):
    price = SomePrice(usd_currency, Decimal('100.00'), Date(2023, 10, 1))
    result = price.floor_divide(0)
    assert result == NoPrice
