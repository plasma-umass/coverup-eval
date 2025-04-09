# file pypara/monetary.py:692-693
# lines [692, 693]
# branches []

import pytest
from pypara.monetary import Money

class NoneMoney(Money):
    def with_dov(self, dov) -> "Money":
        return self

def test_none_money_with_dov():
    from datetime import date as Date

    none_money = NoneMoney()
    dov = Date.today()
    
    result = none_money.with_dov(dov)
    
    assert result is none_money
