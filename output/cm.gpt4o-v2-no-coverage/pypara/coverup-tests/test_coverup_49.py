# file: pypara/monetary.py:389-391
# asked: {"lines": [389, 390, 391], "branches": []}
# gained: {"lines": [389, 390], "branches": []}

import pytest
from pypara.monetary import Money
from pypara.commons.numbers import Numeric

class ConcreteMoney(Money):
    def __floordiv__(self, other: Numeric) -> 'ConcreteMoney':
        return self

def test_floordiv():
    money = ConcreteMoney()
    result = money // 1
    assert isinstance(result, ConcreteMoney)
