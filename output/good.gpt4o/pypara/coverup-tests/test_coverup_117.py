# file pypara/monetary.py:1366-1367
# lines [1366, 1367]
# branches []

import pytest
from pypara.monetary import Price
from typing import Union

Numeric = Union[int, float]

class TestNonePrice:
    def test_divide(self):
        class NonePrice(Price):
            def divide(self, other: Numeric) -> "Price":
                return self

        none_price = NonePrice()
        result = none_price.divide(10)
        assert result is none_price
