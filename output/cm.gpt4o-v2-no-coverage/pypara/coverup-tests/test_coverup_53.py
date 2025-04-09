# file: pypara/monetary.py:208-215
# asked: {"lines": [208, 209, 215], "branches": []}
# gained: {"lines": [208, 209], "branches": []}

import pytest
from pypara.monetary import Money
from pypara.commons.numbers import Numeric

class ConcreteMoney(Money):
    def __init__(self, amount):
        self.amount = amount

    def divide(self, other: Numeric) -> "Money":
        if other == 0:
            return UndefinedMoney()
        return ConcreteMoney(self.amount / other)

class UndefinedMoney(Money):
    def divide(self, other: Numeric) -> "Money":
        return self

def test_divide_by_zero():
    money = ConcreteMoney(100)
    result = money.divide(0)
    assert isinstance(result, UndefinedMoney)

def test_divide_by_non_zero():
    money = ConcreteMoney(100)
    result = money.divide(2)
    assert isinstance(result, ConcreteMoney)
    assert result.amount == 50

def test_undefined_money_divide():
    money = UndefinedMoney()
    result = money.divide(2)
    assert isinstance(result, UndefinedMoney)
