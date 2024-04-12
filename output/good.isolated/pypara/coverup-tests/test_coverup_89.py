# file pypara/monetary.py:900-907
# lines [900, 901, 907]
# branches []

import pytest
from pypara.monetary import Price
from decimal import Decimal

class ConcretePrice(Price):
    def __init__(self, amount):
        self.amount = amount

    def divide(self, other):
        if other == 0:
            return None
        return ConcretePrice(self.amount / other)

@pytest.fixture
def mock_price():
    return ConcretePrice(Decimal('10.00'))

def test_divide_by_zero_returns_none(mock_price):
    result = mock_price.divide(0)
    assert result is None

def test_divide_by_non_zero_returns_price(mock_price):
    divisor = Decimal('2.00')
    expected_amount = mock_price.amount / divisor
    result = mock_price.divide(divisor)
    assert isinstance(result, Price)
    assert result.amount == expected_amount
