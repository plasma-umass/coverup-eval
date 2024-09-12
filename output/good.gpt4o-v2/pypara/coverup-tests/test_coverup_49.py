# file: pypara/monetary.py:199-206
# asked: {"lines": [199, 200, 206], "branches": []}
# gained: {"lines": [199, 200, 206], "branches": []}

import pytest
from pypara.monetary import Money
from pypara.commons.numbers import Numeric

def test_money_multiply_not_implemented():
    class TestMoney(Money):
        def __init__(self, amount):
            self.amount = amount

    test_money = TestMoney(100)
    
    with pytest.raises(NotImplementedError):
        test_money.multiply(2)
