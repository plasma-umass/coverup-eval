# file: pypara/monetary.py:644-645
# asked: {"lines": [644, 645], "branches": []}
# gained: {"lines": [644, 645], "branches": []}

import pytest
from pypara.monetary import NoneMoney, Money

class TestNoneMoney:
    def test_round(self):
        none_money = NoneMoney()
        result = none_money.round(2)
        assert result is none_money

    def test_round_default(self):
        none_money = NoneMoney()
        result = none_money.round()
        assert result is none_money
