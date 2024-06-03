# file pypara/monetary.py:909-917
# lines [917]
# branches []

import pytest
from pypara.monetary import Price

def test_price_floor_divide_not_implemented():
    class TestPrice(Price):
        def floor_divide(self, other):
            super().floor_divide(other)
    
    test_price = TestPrice()
    with pytest.raises(NotImplementedError):
        test_price.floor_divide(10)
