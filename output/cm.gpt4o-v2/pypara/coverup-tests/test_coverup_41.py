# file: pypara/monetary.py:133-138
# asked: {"lines": [133, 134, 138], "branches": []}
# gained: {"lines": [133, 134, 138], "branches": []}

import pytest
from pypara.monetary import Money

def test_money_negative_not_implemented():
    class TestMoney(Money):
        def __init__(self, amount):
            self.amount = amount

    money_instance = TestMoney(100)
    with pytest.raises(NotImplementedError):
        money_instance.negative()
