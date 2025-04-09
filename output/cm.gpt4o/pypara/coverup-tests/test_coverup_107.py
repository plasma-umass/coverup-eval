# file pypara/monetary.py:668-669
# lines [668, 669]
# branches []

import pytest
from pypara.monetary import Money

class NoneMoney(Money):
    def divide(self, other) -> "Money":
        return self

def test_none_money_divide():
    none_money = NoneMoney()
    result = none_money.divide(10)
    assert result is none_money
