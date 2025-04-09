# file pypara/monetary.py:882-889
# lines [889]
# branches []

import pytest
from pypara.monetary import Price

def test_price_multiply_not_implemented():
    class TestPrice(Price):
        def multiply(self, other):
            super().multiply(other)
    
    test_price = TestPrice()
    
    with pytest.raises(NotImplementedError):
        test_price.multiply(10)
