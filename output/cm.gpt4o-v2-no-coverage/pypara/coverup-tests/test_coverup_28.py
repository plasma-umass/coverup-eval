# file: pypara/monetary.py:1204-1210
# asked: {"lines": [1204, 1206, 1207, 1208, 1209, 1210], "branches": []}
# gained: {"lines": [1204, 1206, 1207, 1208, 1209, 1210], "branches": []}

import pytest
from decimal import Decimal, DivisionByZero, InvalidOperation
from pypara.monetary import SomePrice, NoPrice
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

@pytest.fixture
def sample_currency():
    return Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)

@pytest.fixture
def sample_date():
    return Date.today()

@pytest.fixture
def sample_price(sample_currency, sample_date):
    return SomePrice(sample_currency, Decimal("100.00"), sample_date)

def test_floor_divide_valid(sample_price):
    result = sample_price.floor_divide(2)
    assert result.qty == Decimal("50.00")
    assert result.ccy == sample_price.ccy
    assert result.dov == sample_price.dov

def test_floor_divide_invalid_operation(sample_price):
    result = sample_price.floor_divide("invalid")
    assert result == NoPrice

def test_floor_divide_division_by_zero(sample_price):
    result = sample_price.floor_divide(0)
    assert result == NoPrice
