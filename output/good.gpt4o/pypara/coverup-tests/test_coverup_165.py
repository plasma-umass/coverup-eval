# file pypara/monetary.py:860-871
# lines [871]
# branches []

import pytest
from pypara.monetary import Price

def test_price_subtract_not_implemented():
    class TestPrice(Price):
        def subtract(self, other: "Price") -> "Price":
            super().subtract(other)
    
    price1 = TestPrice()
    price2 = TestPrice()
    
    with pytest.raises(NotImplementedError):
        price1.subtract(price2)
