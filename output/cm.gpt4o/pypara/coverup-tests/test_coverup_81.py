# file pypara/monetary.py:653-654
# lines [653, 654]
# branches []

import pytest
from pypara.monetary import Money

class NoneMoney(Money):
    def add(self, other: "Money") -> "Money":
        return other

def test_none_money_add():
    class MockMoney(Money):
        def __init__(self, amount):
            self.amount = amount

        def __eq__(self, other):
            return self.amount == other.amount

    none_money = NoneMoney()
    other_money = MockMoney(100)

    result = none_money.add(other_money)

    assert result == other_money
