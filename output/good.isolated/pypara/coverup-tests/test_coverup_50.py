# file pypara/monetary.py:346-348
# lines [346, 347, 348]
# branches []

import pytest
from pypara.monetary import Money

class ConcreteMoney(Money):
    def __int__(self):
        return 42

def test_money_abstract_int_method():
    money = ConcreteMoney()
    assert int(money) == 42
