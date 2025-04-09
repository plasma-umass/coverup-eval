# file: pypara/monetary.py:662-663
# asked: {"lines": [662, 663], "branches": []}
# gained: {"lines": [662, 663], "branches": []}

import pytest
from pypara.monetary import NoneMoney, Money

class TestNoneMoney:
    def test_scalar_subtract(self):
        none_money = NoneMoney()
        result = none_money.scalar_subtract(10)
        assert result is none_money

    def test_scalar_subtract_with_zero(self):
        none_money = NoneMoney()
        result = none_money.scalar_subtract(0)
        assert result is none_money

    def test_scalar_subtract_with_negative(self):
        none_money = NoneMoney()
        result = none_money.scalar_subtract(-5)
        assert result is none_money
