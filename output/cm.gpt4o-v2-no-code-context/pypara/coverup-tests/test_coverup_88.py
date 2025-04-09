# file: pypara/monetary.py:677-678
# asked: {"lines": [677, 678], "branches": []}
# gained: {"lines": [677], "branches": []}

import pytest
from pypara.monetary import Money

class NoneMoney(Money):
    def lte(self, other: "Money") -> bool:
        return True

def test_none_money_lte():
    none_money = NoneMoney()
    other_money = Money()
    
    assert none_money.lte(other_money) == True
