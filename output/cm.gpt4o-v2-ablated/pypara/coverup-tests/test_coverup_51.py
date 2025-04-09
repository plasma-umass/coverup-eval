# file: pypara/monetary.py:1366-1367
# asked: {"lines": [1366, 1367], "branches": []}
# gained: {"lines": [1366, 1367], "branches": []}

import pytest
from pypara.monetary import NonePrice, Price

class TestNonePrice:
    def test_divide(self):
        none_price = NonePrice()
        result = none_price.divide(10)
        assert result is none_price

    def test_divide_with_zero(self):
        none_price = NonePrice()
        result = none_price.divide(0)
        assert result is none_price

    def test_divide_with_negative(self):
        none_price = NonePrice()
        result = none_price.divide(-5)
        assert result is none_price
