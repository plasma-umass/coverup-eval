# file: pypara/monetary.py:1354-1355
# asked: {"lines": [1354, 1355], "branches": []}
# gained: {"lines": [1354, 1355], "branches": []}

import pytest
from pypara.monetary import NonePrice, Price

class MockPrice(Price):
    def __init__(self, value):
        self.value = value

    def __neg__(self):
        return MockPrice(-self.value)

    def __eq__(self, other):
        return self.value == other.value

def test_noneprice_subtract():
    none_price = NonePrice()
    other_price = MockPrice(100)

    result = none_price.subtract(other_price)

    assert isinstance(result, MockPrice)
    assert result.value == -100
