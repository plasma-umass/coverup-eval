# file: pypara/monetary.py:1351-1352
# asked: {"lines": [1351, 1352], "branches": []}
# gained: {"lines": [1351, 1352], "branches": []}

import pytest
from pypara.monetary import NonePrice, Price

class TestNonePrice:
    def test_scalar_add(self):
        none_price = NonePrice()
        result = none_price.scalar_add(10)
        assert result is none_price
