# file: pypara/monetary.py:680-681
# asked: {"lines": [681], "branches": []}
# gained: {"lines": [681], "branches": []}

import pytest
from pypara.monetary import NoneMoney, Money

class TestNoneMoney:
    def test_gt_with_none_money(self):
        none_money = NoneMoney()
        other_money = Money()
        assert not none_money.gt(other_money)

    def test_gt_with_money_subclass(self):
        class SubMoney(Money):
            pass

        none_money = NoneMoney()
        sub_money = SubMoney()
        assert not none_money.gt(sub_money)
