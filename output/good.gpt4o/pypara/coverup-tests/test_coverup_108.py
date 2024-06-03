# file pypara/monetary.py:1159-1162
# lines [1159, 1161, 1162]
# branches []

import pytest
from decimal import Decimal
from datetime import date as Date
from collections import namedtuple

# Assuming Currency, Price, and Numeric are defined somewhere in pypara.monetary
from pypara.monetary import Currency, Price, Numeric

# Mocking the necessary classes for the test
class MockCurrency(Currency):
    def __init__(self):
        super().__init__('USD', 'US Dollar', 2, 'fiat', Decimal('0.01'), None)

class MockPrice(Price):
    pass

SomePriceBase = namedtuple("SomePriceBase", ["ccy", "qty", "dov"])

class SomePrice(MockPrice, SomePriceBase):
    def scalar_add(self, other: Numeric) -> "Price":
        c, q, d = self
        return SomePrice(c, q + Decimal(other), d)

@pytest.fixture
def some_price():
    return SomePrice(MockCurrency(), Decimal('100.00'), Date(2023, 1, 1))

def test_scalar_add_with_decimal(some_price):
    result = some_price.scalar_add(Decimal('50.00'))
    assert result.qty == Decimal('150.00')
    assert result.ccy == some_price.ccy
    assert result.dov == some_price.dov

def test_scalar_add_with_int(some_price):
    result = some_price.scalar_add(50)
    assert result.qty == Decimal('150.00')
    assert result.ccy == some_price.ccy
    assert result.dov == some_price.dov

def test_scalar_add_with_float(some_price):
    result = some_price.scalar_add(50.0)
    assert result.qty == Decimal('150.00')
    assert result.ccy == some_price.ccy
    assert result.dov == some_price.dov
