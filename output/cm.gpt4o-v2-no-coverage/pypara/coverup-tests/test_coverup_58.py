# file: pypara/monetary.py:381-383
# asked: {"lines": [381, 382, 383], "branches": []}
# gained: {"lines": [381, 382], "branches": []}

import pytest
from pypara.monetary import Money
from pypara.commons.numbers import Numeric

class ConcreteMoney(Money):
    def __init__(self, amount):
        self.amount = amount

    def __mul__(self, other: Numeric) -> 'ConcreteMoney':
        return ConcreteMoney(self.amount * other)

def test_money_mul():
    money = ConcreteMoney(10)
    result = money * 2
    assert isinstance(result, ConcreteMoney)
    assert result.amount == 20
