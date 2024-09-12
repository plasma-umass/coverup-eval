# file: pypara/monetary.py:190-197
# asked: {"lines": [190, 191, 197], "branches": []}
# gained: {"lines": [190, 191, 197], "branches": []}

import pytest
from pypara.monetary import Money
from pypara.commons.numbers import Numeric

class ConcreteMoney(Money):
    def scalar_subtract(self, other: Numeric) -> "Money":
        return self  # Dummy implementation for testing

def test_scalar_subtract_not_implemented():
    money = Money()
    with pytest.raises(NotImplementedError):
        money.scalar_subtract(10)

def test_concrete_money_scalar_subtract():
    money = ConcreteMoney()
    result = money.scalar_subtract(10)
    assert result is money

