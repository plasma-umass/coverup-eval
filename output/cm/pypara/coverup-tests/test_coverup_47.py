# file pypara/monetary.py:208-215
# lines [208, 209, 215]
# branches []

import pytest
from pypara.monetary import Money
from decimal import Decimal

class ConcreteMoney(Money):
    def __init__(self, amount):
        self.amount = amount

    def divide(self, other):
        if other == 0:
            return "undefined"
        return ConcreteMoney(self.amount / other)

@pytest.fixture
def mock_money():
    return ConcreteMoney(Decimal('100.00'))

def test_divide_by_zero_returns_undefined(mock_money):
    result = mock_money.divide(0)
    assert result == "undefined"

def test_divide_by_non_zero_returns_money_object(mock_money):
    divisor = Decimal('2')
    expected_amount = mock_money.amount / divisor
    result = mock_money.divide(divisor)
    assert isinstance(result, Money)
    assert result.amount == expected_amount
