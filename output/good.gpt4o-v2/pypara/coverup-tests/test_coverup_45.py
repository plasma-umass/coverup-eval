# file: pypara/monetary.py:177-188
# asked: {"lines": [177, 178, 188], "branches": []}
# gained: {"lines": [177, 178, 188], "branches": []}

import pytest
from pypara.monetary import Money

def test_money_subtract_not_implemented():
    class TestMoney(Money):
        def __init__(self, amount, currency):
            self.amount = amount
            self.currency = currency

    money1 = TestMoney(100, 'USD')
    money2 = TestMoney(50, 'USD')

    with pytest.raises(NotImplementedError):
        money1.subtract(money2)
