# file: pypara/monetary.py:369-371
# asked: {"lines": [369, 370, 371], "branches": []}
# gained: {"lines": [369, 370], "branches": []}

import pytest
from pypara.monetary import Money

def test_money_pos():
    class ConcreteMoney(Money):
        def __pos__(self):
            return self

    money_instance = ConcreteMoney()
    assert +money_instance is money_instance
