# file pypara/monetary.py:677-678
# lines [677, 678]
# branches []

import pytest
from pypara.monetary import Money

class NoneMoney(Money):
    def lte(self, other: "Money") -> bool:
        return True

def test_none_money_lte(mocker):
    none_money = NoneMoney()
    other_money = mocker.Mock(spec=Money)
    
    assert none_money.lte(other_money) == True
