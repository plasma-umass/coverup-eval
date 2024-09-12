# file: pypara/monetary.py:1369-1370
# asked: {"lines": [1369, 1370], "branches": []}
# gained: {"lines": [1369, 1370], "branches": []}

import pytest
from pypara.monetary import NonePrice, Price

class TestNonePrice:
    def test_floor_divide(self):
        none_price = NonePrice()
        other = 10  # This can be any numeric value
        result = none_price.floor_divide(other)
        
        assert result is none_price  # Ensure the method returns the instance itself
