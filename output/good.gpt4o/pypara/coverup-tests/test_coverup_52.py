# file pypara/monetary.py:389-391
# lines [389, 390, 391]
# branches []

import pytest
from pypara.monetary import Money
from decimal import Decimal

class ConcreteMoney(Money):
    def __init__(self, amount):
        self.amount = amount

    def __floordiv__(self, other) -> "ConcreteMoney":
        if not isinstance(other, (int, float, Decimal)):
            raise TypeError("Operand must be a numeric type")
        return ConcreteMoney(self.amount // other)

def test_floordiv():
    money = ConcreteMoney(100)
    result = money // 3
    assert isinstance(result, ConcreteMoney)
    assert result.amount == 33

    with pytest.raises(TypeError):
        money // "invalid"

    with pytest.raises(ZeroDivisionError):
        money // 0
