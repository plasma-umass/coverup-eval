# file: pypara/monetary.py:851-858
# asked: {"lines": [858], "branches": []}
# gained: {"lines": [858], "branches": []}

import pytest
from pypara.monetary import Price
from pypara.commons.numbers import Numeric

def test_price_scalar_add_not_implemented():
    class TestPrice(Price):
        def scalar_add(self, other: Numeric) -> 'Price':
            return super().scalar_add(other)
    
    test_price = TestPrice()
    with pytest.raises(NotImplementedError):
        test_price.scalar_add(10)
