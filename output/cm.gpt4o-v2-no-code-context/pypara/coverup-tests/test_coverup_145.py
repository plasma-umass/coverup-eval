# file: pypara/monetary.py:838-849
# asked: {"lines": [849], "branches": []}
# gained: {"lines": [849], "branches": []}

import pytest
from pypara.monetary import Price

class TestPrice:
    def test_add_not_implemented(self):
        class TestPriceImplementation(Price):
            def add(self, other: "Price") -> "Price":
                super().add(other)
        
        price1 = TestPriceImplementation()
        price2 = TestPriceImplementation()
        
        with pytest.raises(NotImplementedError):
            price1.add(price2)
