# file: pypara/monetary.py:860-871
# asked: {"lines": [871], "branches": []}
# gained: {"lines": [871], "branches": []}

import pytest
from pypara.monetary import Price

class TestPrice:
    def test_subtract_not_implemented(self):
        class TestPriceImplementation(Price):
            def subtract(self, other: "Price") -> "Price":
                super().subtract(other)
        
        price1 = TestPriceImplementation()
        price2 = TestPriceImplementation()
        
        with pytest.raises(NotImplementedError):
            price1.subtract(price2)
