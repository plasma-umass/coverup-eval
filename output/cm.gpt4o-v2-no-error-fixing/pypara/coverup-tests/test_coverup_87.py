# file: pypara/monetary.py:838-849
# asked: {"lines": [849], "branches": []}
# gained: {"lines": [849], "branches": []}

import pytest
from pypara.monetary import Price

def test_price_add_not_implemented():
    class TestPrice(Price):
        def add(self, other: 'Price') -> 'Price':
            return super().add(other)
    
    price1 = TestPrice()
    price2 = TestPrice()
    
    with pytest.raises(NotImplementedError):
        price1.add(price2)
