# file pypara/monetary.py:199-206
# lines [206]
# branches []

import pytest
from pypara.monetary import Money
from decimal import Decimal

class ConcreteMoney(Money):
    def multiply(self, other):
        return super().multiply(other)

def test_money_multiply_not_implemented(mocker):
    money = ConcreteMoney()
    with pytest.raises(NotImplementedError):
        money.multiply(Decimal('2.0'))
