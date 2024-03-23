# file pypara/monetary.py:208-215
# lines [215]
# branches []

import pytest
from pypara.monetary import Money

class ConcreteMoney(Money):
    def divide(self, other):
        return super().divide(other)

def test_money_divide_not_implemented(mocker):
    concrete_money = ConcreteMoney()
    with pytest.raises(NotImplementedError):
        concrete_money.divide(2)
