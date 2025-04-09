# file: pypara/monetary.py:1357-1358
# asked: {"lines": [1357, 1358], "branches": []}
# gained: {"lines": [1357, 1358], "branches": []}

import pytest
from pypara.monetary import NonePrice, Price

class TestNonePrice:
    def test_scalar_subtract(self):
        none_price = NonePrice()
        result = none_price.scalar_subtract(10)
        assert result is none_price
