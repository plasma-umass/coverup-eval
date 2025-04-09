# file: pypara/monetary.py:385-387
# asked: {"lines": [385, 386, 387], "branches": []}
# gained: {"lines": [385, 386], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import Money
from pypara.commons.numbers import Numeric

class ConcreteMoney(Money):
    def __init__(self, amount):
        self.amount = amount

    def __truediv__(self, other: Numeric) -> "ConcreteMoney":
        if not isinstance(other, (int, float, Decimal)):
            raise TypeError("Unsupported type for division")
        return ConcreteMoney(self.amount / other)

def test_truediv_with_int():
    money = ConcreteMoney(100)
    result = money / 2
    assert isinstance(result, ConcreteMoney)
    assert result.amount == 50

def test_truediv_with_float():
    money = ConcreteMoney(100)
    result = money / 2.0
    assert isinstance(result, ConcreteMoney)
    assert result.amount == 50.0

def test_truediv_with_decimal():
    money = ConcreteMoney(Decimal('100.0'))
    result = money / Decimal('2.0')
    assert isinstance(result, ConcreteMoney)
    assert result.amount == Decimal('50.0')

def test_truediv_with_invalid_type():
    money = ConcreteMoney(100)
    with pytest.raises(TypeError):
        money / "invalid"
