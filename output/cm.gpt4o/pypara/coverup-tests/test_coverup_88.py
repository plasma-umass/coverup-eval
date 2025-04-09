# file pypara/monetary.py:1330-1331
# lines [1330, 1331]
# branches []

import pytest
from pypara.monetary import Price

class TestNonePrice:
    def test_abs_method(self):
        class NonePrice(Price):
            def abs(self) -> "Price":
                return self

        none_price = NonePrice()
        result = none_price.abs()
        
        assert result is none_price
