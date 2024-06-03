# file pypara/monetary.py:900-907
# lines [907]
# branches []

import pytest
from pypara.monetary import Price

def test_price_divide_not_implemented():
    class TestPrice(Price):
        def divide(self, other):
            super().divide(other)
    
    test_price = TestPrice()
    
    with pytest.raises(NotImplementedError):
        test_price.divide(10)
