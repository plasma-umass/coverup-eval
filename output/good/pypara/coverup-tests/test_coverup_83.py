# file pypara/monetary.py:385-387
# lines [385, 386, 387]
# branches []

import pytest
from decimal import Decimal
from pypara.monetary import Money
from numbers import Number

class ConcreteMoney(Money):
    def __init__(self, amount: Number):
        self.amount = Decimal(amount)

    def __truediv__(self, other: Number) -> "ConcreteMoney":
        if other == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return ConcreteMoney(self.amount / Decimal(other))

def test_money_division():
    money = ConcreteMoney(100)
    result = money / 2
    assert isinstance(result, Money)
    assert result.amount == Decimal('50')

    with pytest.raises(ZeroDivisionError):
        money / 0

def test_money_division_by_decimal():
    money = ConcreteMoney(100)
    result = money / Decimal('2.5')
    assert isinstance(result, Money)
    assert result.amount == Decimal('40')

# Cleanup is not necessary for this test as we are not modifying any external state
# or shared resources. The ConcreteMoney instances are local to the test functions.
