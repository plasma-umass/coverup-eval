# file: pypara/monetary.py:665-666
# asked: {"lines": [665, 666], "branches": []}
# gained: {"lines": [665, 666], "branches": []}

import pytest
from pypara.monetary import NoneMoney, Money

class TestNoneMoney:
    def test_multiply(self):
        none_money = NoneMoney()
        result = none_money.multiply(10)
        assert result is none_money

    def test_multiply_with_zero(self):
        none_money = NoneMoney()
        result = none_money.multiply(0)
        assert result is none_money

    def test_multiply_with_negative(self):
        none_money = NoneMoney()
        result = none_money.multiply(-5)
        assert result is none_money

    def test_multiply_with_float(self):
        none_money = NoneMoney()
        result = none_money.multiply(2.5)
        assert result is none_money
