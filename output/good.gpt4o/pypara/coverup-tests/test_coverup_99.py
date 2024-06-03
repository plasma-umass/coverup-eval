# file pypara/monetary.py:1348-1349
# lines [1348, 1349]
# branches []

import pytest
from pypara.monetary import Price, NonePrice

def test_none_price_add():
    class MockPrice(Price):
        def __init__(self, value):
            self.value = value

        def __eq__(self, other):
            return isinstance(other, MockPrice) and self.value == other.value

    none_price = NonePrice()
    other_price = MockPrice(100)

    result = none_price.add(other_price)

    assert result == other_price
