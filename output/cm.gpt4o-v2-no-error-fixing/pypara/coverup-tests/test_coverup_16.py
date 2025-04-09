# file: pypara/monetary.py:199-206
# asked: {"lines": [199, 200, 206], "branches": []}
# gained: {"lines": [199, 200, 206], "branches": []}

import pytest
from pypara.monetary import Money
from pypara.commons.numbers import Numeric

class ConcreteMoney(Money):
    def multiply(self, other: Numeric) -> "Money":
        return self

def test_multiply_not_implemented():
    money = Money()
    with pytest.raises(NotImplementedError):
        money.multiply(10)

def test_concrete_multiply():
    money = ConcreteMoney()
    result = money.multiply(10)
    assert result is money
