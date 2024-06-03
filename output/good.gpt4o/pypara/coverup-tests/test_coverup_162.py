# file pypara/monetary.py:851-858
# lines [858]
# branches []

import pytest
from pypara.monetary import Price

def test_price_scalar_add_not_implemented():
    class TestPrice(Price):
        def scalar_add(self, other):
            super().scalar_add(other)
    
    test_price = TestPrice()
    with pytest.raises(NotImplementedError):
        test_price.scalar_add(10)
