# file pypara/monetary.py:126-131
# lines [131]
# branches []

import pytest
from pypara.monetary import Money

class ConcreteMoney(Money):
    def abs(self):
        return super().abs()

def test_money_abs_not_implemented():
    money = ConcreteMoney()
    with pytest.raises(NotImplementedError):
        money.abs()
