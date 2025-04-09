# file pypara/monetary.py:838-849
# lines [849]
# branches []

import pytest
from pypara.monetary import Price

def test_price_add_not_implemented():
    class TestPrice(Price):
        def add(self, other: "Price") -> "Price":
            super().add(other)
    
    price1 = TestPrice()
    price2 = TestPrice()
    
    with pytest.raises(NotImplementedError):
        price1.add(price2)
