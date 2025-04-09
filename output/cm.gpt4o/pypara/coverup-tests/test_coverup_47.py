# file pypara/monetary.py:190-197
# lines [190, 191, 197]
# branches []

import pytest
from abc import ABC, abstractmethod
from pypara.monetary import Money

class ConcreteMoney(Money):
    def scalar_subtract(self, other):
        return self

def test_scalar_subtract_not_implemented():
    class IncompleteMoney(Money):
        pass

    with pytest.raises(NotImplementedError):
        money = IncompleteMoney()
        money.scalar_subtract(10)

def test_scalar_subtract_implemented():
    money = ConcreteMoney()
    result = money.scalar_subtract(10)
    assert result is money
