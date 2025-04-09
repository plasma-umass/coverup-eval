# file pypara/monetary.py:644-645
# lines [644, 645]
# branches []

import pytest
from pypara.monetary import Money

class NoneMoney(Money):
    def round(self, ndigits: int = 0) -> "Money":
        return self

def test_none_money_round():
    none_money = NoneMoney()
    rounded_money = none_money.round(2)
    
    assert rounded_money is none_money
    assert isinstance(rounded_money, NoneMoney)
