# file: pypara/monetary.py:168-175
# asked: {"lines": [168, 169, 175], "branches": []}
# gained: {"lines": [168, 169, 175], "branches": []}

import pytest
from pypara.monetary import Money
from pypara.commons.numbers import Numeric

class ConcreteMoney(Money):
    def scalar_add(self, other: Numeric) -> "Money":
        return self

def test_scalar_add_not_implemented():
    class AbstractMoney(Money):
        pass

    money = AbstractMoney()
    with pytest.raises(NotImplementedError):
        money.scalar_add(10)

def test_scalar_add_implemented():
    money = ConcreteMoney()
    result = money.scalar_add(10)
    assert result is money
