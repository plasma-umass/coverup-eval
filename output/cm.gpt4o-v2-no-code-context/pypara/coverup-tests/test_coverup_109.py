# file: pypara/monetary.py:680-681
# asked: {"lines": [680, 681], "branches": []}
# gained: {"lines": [680], "branches": []}

import pytest
from pypara.monetary import Money

class NoneMoney(Money):
    def gt(self, other: "Money") -> bool:
        return False

class TestNoneMoney:
    def test_none_money_gt(self):
        none_money = NoneMoney()
        other_money = Money()
        
        assert not none_money.gt(other_money)
