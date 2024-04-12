# file pypara/monetary.py:119-124
# lines [119, 120, 124]
# branches []

import pytest
from pypara.monetary import Money, MonetaryOperationException

class ConcreteMoney(Money):
    def as_integer(self) -> int:
        return 42

def test_money_as_integer():
    money = ConcreteMoney()
    assert money.as_integer() == 42

def test_money_as_integer_not_implemented():
    money = Money()
    with pytest.raises(NotImplementedError):
        money.as_integer()
