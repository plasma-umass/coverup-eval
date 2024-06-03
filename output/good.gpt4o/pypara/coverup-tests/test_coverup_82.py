# file pypara/monetary.py:674-675
# lines [674, 675]
# branches []

import pytest
from pypara.monetary import Money

class NoneMoney(Money):
    def lt(self, other: "Money") -> bool:
        return other.defined

def test_none_money_lt():
    class MockMoney(Money):
        def __init__(self, defined):
            self.defined = defined

    none_money = NoneMoney()
    other_money_defined = MockMoney(defined=True)
    other_money_undefined = MockMoney(defined=False)

    assert none_money.lt(other_money_defined) is True
    assert none_money.lt(other_money_undefined) is False
