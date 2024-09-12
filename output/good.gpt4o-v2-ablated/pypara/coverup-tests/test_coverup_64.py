# file: pypara/monetary.py:677-678
# asked: {"lines": [678], "branches": []}
# gained: {"lines": [678], "branches": []}

import pytest
from pypara.monetary import NoneMoney, Money

class TestNoneMoney:
    def test_lte_with_none_money(self):
        none_money = NoneMoney()
        other_money = NoneMoney()
        assert none_money.lte(other_money) is True

    def test_lte_with_other_money(self, mocker):
        none_money = NoneMoney()
        other_money = mocker.Mock(spec=Money)
        assert none_money.lte(other_money) is True
