# file pypara/monetary.py:1342-1343
# lines [1342, 1343]
# branches []

import pytest
from pypara.monetary import Price

class TestNonePrice:
    def test_negative(self):
        class NonePrice(Price):
            def negative(self) -> "Price":
                return self

        none_price = NonePrice()
        result = none_price.negative()
        
        assert result is none_price
