# file pypara/monetary.py:1354-1355
# lines [1354, 1355]
# branches []

import pytest
from pypara.monetary import Price, NonePrice

def test_noneprice_subtract():
    class MockPrice(Price):
        def __init__(self, value):
            self.value = value

        def __neg__(self):
            return MockPrice(-self.value)

        def __eq__(self, other):
            return self.value == other.value

    none_price = NonePrice()
    other_price = MockPrice(100)

    result = none_price.subtract(other_price)

    assert result == MockPrice(-100)
