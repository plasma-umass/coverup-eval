# file: pypara/monetary.py:208-215
# asked: {"lines": [208, 209, 215], "branches": []}
# gained: {"lines": [208, 209, 215], "branches": []}

import pytest
from pypara.monetary import Money
from pypara.commons.numbers import Numeric

class ConcreteMoney(Money):
    def divide(self, other: Numeric) -> 'Money':
        if other == 0:
            raise ValueError("Division by zero is undefined")
        return self  # Simplified for testing purposes

def test_divide_not_implemented():
    money = Money()
    with pytest.raises(NotImplementedError):
        money.divide(1)

def test_concrete_divide():
    money = ConcreteMoney()
    result = money.divide(1)
    assert result is money

def test_concrete_divide_by_zero():
    money = ConcreteMoney()
    with pytest.raises(ValueError, match="Division by zero is undefined"):
        money.divide(0)
