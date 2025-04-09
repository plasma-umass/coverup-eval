# file pypara/monetary.py:647-648
# lines [647, 648]
# branches []

import pytest
from pypara.monetary import Money

class NoneMoney(Money):
    def negative(self) -> "Money":
        return self

def test_none_money_negative():
    none_money = NoneMoney()
    result = none_money.negative()
    assert result is none_money
