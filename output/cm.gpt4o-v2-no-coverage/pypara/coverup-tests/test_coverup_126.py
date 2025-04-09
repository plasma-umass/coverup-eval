# file: pypara/monetary.py:659-660
# asked: {"lines": [659, 660], "branches": []}
# gained: {"lines": [659, 660], "branches": []}

import pytest
from pypara.monetary import NoneMoney, Money

class MockMoney(Money):
    def __neg__(self):
        return self
    
    def __eq__(self, other):
        return isinstance(other, MockMoney)

def test_none_money_subtract():
    none_money = NoneMoney()
    other_money = MockMoney()
    
    result = none_money.subtract(other_money)
    
    assert result == other_money
