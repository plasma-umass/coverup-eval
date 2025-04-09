# file pypara/monetary.py:635-636
# lines [635, 636]
# branches []

import pytest
from pypara.monetary import Money

class NoneMoney(Money):
    def abs(self) -> "Money":
        return self

def test_none_money_abs():
    none_money = NoneMoney()
    result = none_money.abs()
    assert result is none_money
