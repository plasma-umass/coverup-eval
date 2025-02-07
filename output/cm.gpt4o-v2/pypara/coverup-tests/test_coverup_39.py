# file: pypara/monetary.py:140-145
# asked: {"lines": [140, 141, 145], "branches": []}
# gained: {"lines": [140, 141, 145], "branches": []}

import pytest
from pypara.monetary import Money

def test_money_positive_not_implemented():
    class TestMoney(Money):
        def __init__(self, amount):
            self.amount = amount

    test_money = TestMoney(100)
    
    with pytest.raises(NotImplementedError):
        test_money.positive()
