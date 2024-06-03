# file pypara/monetary.py:650-651
# lines [650, 651]
# branches []

import pytest
from pypara.monetary import Money

class NoneMoney(Money):
    def positive(self) -> "Money":
        return self

def test_none_money_positive():
    none_money = NoneMoney()
    result = none_money.positive()
    assert result is none_money
