# file: pypara/monetary.py:683-684
# asked: {"lines": [683, 684], "branches": []}
# gained: {"lines": [683, 684], "branches": []}

import pytest
from pypara.monetary import NoneMoney, Money

class MockMoney:
    def __init__(self, undefined):
        self.undefined = undefined

def test_none_money_gte():
    none_money = NoneMoney()
    other_money = MockMoney(undefined=True)
    
    assert none_money.gte(other_money) == True

    other_money = MockMoney(undefined=False)
    
    assert none_money.gte(other_money) == False
