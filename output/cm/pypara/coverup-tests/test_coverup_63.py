# file pypara/monetary.py:381-383
# lines [381, 382, 383]
# branches []

import pytest
from decimal import Decimal
from pypara.monetary import Money
from numbers import Number

class ConcreteMoney(Money):
    def __init__(self, amount):
        if not isinstance(amount, Number):
            raise ValueError("amount must be a number")
        self.amount = amount

    def __mul__(self, other):
        if not isinstance(other, Number):
            raise ValueError("Multiplier must be a number")
        return ConcreteMoney(self.amount * other)

@pytest.fixture
def mock_money():
    return ConcreteMoney(10)

def test_money_multiplication(mock_money):
    # Test multiplication with an int
    result = mock_money * 2
    assert isinstance(result, Money)
    assert result.amount == 20

    # Test multiplication with a float
    result = mock_money * 2.5
    assert isinstance(result, Money)
    assert result.amount == 25

    # Test multiplication with a Decimal
    result = mock_money * Decimal('3.5')
    assert isinstance(result, Money)
    assert result.amount == 35

    # Test multiplication with an invalid type should raise ValueError
    with pytest.raises(ValueError):
        mock_money * "invalid"

# Clean up is not necessary as each test function will get its own instance of ConcreteMoney
# due to the fixture scope being function-level by default.
