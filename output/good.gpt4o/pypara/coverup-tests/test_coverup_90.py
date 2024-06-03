# file pypara/monetary.py:680-681
# lines [680, 681]
# branches []

import pytest
from pypara.monetary import Money

class NoneMoney(Money):
    def gt(self, other: "Money") -> bool:
        return False

def test_none_money_gt(mocker):
    none_money = NoneMoney()
    other_money = mocker.Mock(spec=Money)
    
    assert not none_money.gt(other_money)
