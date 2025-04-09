# file: pypara/monetary.py:668-669
# asked: {"lines": [669], "branches": []}
# gained: {"lines": [669], "branches": []}

import pytest
from pypara.monetary import NoneMoney, Money

class TestNoneMoney:
    def test_divide(self):
        none_money = NoneMoney()
        result = none_money.divide(10)
        assert result is none_money

    def test_divide_with_zero(self):
        none_money = NoneMoney()
        result = none_money.divide(0)
        assert result is none_money

    def test_divide_with_negative(self):
        none_money = NoneMoney()
        result = none_money.divide(-5)
        assert result is none_money
