# file pypara/monetary.py:140-145
# lines [145]
# branches []

import pytest
from pypara.monetary import Money

class ConcreteMoney(Money):
    def positive(self):
        return super().positive()

def test_money_positive_not_implemented():
    money = ConcreteMoney()
    with pytest.raises(NotImplementedError):
        money.positive()
