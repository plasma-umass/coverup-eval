# file pypara/monetary.py:659-660
# lines [659, 660]
# branches []

import pytest
from pypara.monetary import Money

class NoneMoney(Money):
    def subtract(self, other: "Money") -> "Money":
        return -other

def test_none_money_subtract():
    class MockMoney(Money):
        def __neg__(self):
            return self

    none_money = NoneMoney()
    mock_money = MockMoney()

    result = none_money.subtract(mock_money)
    
    assert result is mock_money
