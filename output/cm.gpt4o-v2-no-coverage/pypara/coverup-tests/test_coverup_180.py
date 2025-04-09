# file: pypara/monetary.py:1187-1190
# asked: {"lines": [1189, 1190], "branches": []}
# gained: {"lines": [1189, 1190], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

@pytest.fixture
def sample_price():
    usd = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    return SomePrice(usd, Decimal("100.00"), Date(2023, 1, 1))

def test_multiply_with_int(sample_price):
    result = sample_price.multiply(2)
    assert result.qty == Decimal("200.00")
    assert result.ccy == sample_price.ccy
    assert result.dov == sample_price.dov

def test_multiply_with_float(sample_price):
    result = sample_price.multiply(2.5)
    assert result.qty == Decimal("250.00")
    assert result.ccy == sample_price.ccy
    assert result.dov == sample_price.dov

def test_multiply_with_decimal(sample_price):
    result = sample_price.multiply(Decimal("1.5"))
    assert result.qty == Decimal("150.00")
    assert result.ccy == sample_price.ccy
    assert result.dov == sample_price.dov

def test_multiply_with_negative(sample_price):
    result = sample_price.multiply(-1)
    assert result.qty == Decimal("-100.00")
    assert result.ccy == sample_price.ccy
    assert result.dov == sample_price.dov

def test_multiply_with_zero(sample_price):
    result = sample_price.multiply(0)
    assert result.qty == Decimal("0.00")
    assert result.ccy == sample_price.ccy
    assert result.dov == sample_price.dov
