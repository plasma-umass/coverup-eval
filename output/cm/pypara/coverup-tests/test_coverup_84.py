# file pypara/monetary.py:873-880
# lines [873, 874, 880]
# branches []

import pytest
from pypara.monetary import Price
from decimal import Decimal

class ConcretePrice(Price):
    def __init__(self, amount):
        self.amount = amount

    def scalar_subtract(self, other):
        if self.amount is None:
            return self
        return ConcretePrice(self.amount - Decimal(other))

@pytest.fixture
def price():
    return ConcretePrice(Decimal('10.00'))

def test_scalar_subtract_with_concrete_price(price):
    result = price.scalar_subtract(5)
    assert result.amount == Decimal('5.00')

def test_scalar_subtract_with_undefined_price():
    undefined_price = ConcretePrice(None)
    result = undefined_price.scalar_subtract(5)
    assert result.amount is None
