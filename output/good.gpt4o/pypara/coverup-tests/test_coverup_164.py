# file pypara/monetary.py:873-880
# lines [880]
# branches []

import pytest
from pypara.monetary import Price

def test_price_scalar_subtract_not_implemented():
    class TestPrice(Price):
        def scalar_subtract(self, other):
            super().scalar_subtract(other)
    
    test_price = TestPrice()
    with pytest.raises(NotImplementedError):
        test_price.scalar_subtract(10)
