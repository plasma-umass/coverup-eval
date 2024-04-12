# file pypara/monetary.py:882-889
# lines [882, 883, 889]
# branches []

import pytest
from pypara.monetary import Price
from decimal import Decimal

class ConcretePrice(Price):
    def __init__(self, amount):
        self.amount = amount

    def multiply(self, other: Decimal) -> "Price":
        if self.amount is None:
            return self
        return ConcretePrice(self.amount * other)

@pytest.fixture
def numeric_value():
    return Decimal('1.0')

@pytest.fixture
def price_value():
    return ConcretePrice(Decimal('10.00'))

@pytest.fixture
def undefined_price():
    return ConcretePrice(None)

def test_price_multiply_with_numeric(price_value, numeric_value):
    result = price_value.multiply(numeric_value)
    assert isinstance(result, Price)
    assert result.amount == price_value.amount * numeric_value

def test_price_multiply_with_undefined_price(undefined_price, numeric_value):
    result = undefined_price.multiply(numeric_value)
    assert isinstance(result, Price)
    assert result.amount is None
