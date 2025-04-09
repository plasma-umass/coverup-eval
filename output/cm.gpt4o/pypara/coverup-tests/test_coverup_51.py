# file pypara/monetary.py:381-383
# lines [381, 382, 383]
# branches []

import pytest
from pypara.monetary import Money
from decimal import Decimal

class ConcreteMoney(Money):
    def __init__(self, amount):
        self.amount = amount

    def __mul__(self, other) -> "ConcreteMoney":
        if not isinstance(other, (int, float, Decimal)):
            raise TypeError("Multiplier must be a numeric type")
        return ConcreteMoney(self.amount * other)

def test_money_mul():
    money = ConcreteMoney(100)
    result = money.__mul__(2)
    assert isinstance(result, ConcreteMoney)
    assert result.amount == 200

    result = money.__mul__(Decimal('1.5'))
    assert isinstance(result, ConcreteMoney)
    assert result.amount == Decimal('150')

    with pytest.raises(TypeError):
        money.__mul__('invalid')
