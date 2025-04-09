# file: pypara/monetary.py:873-880
# asked: {"lines": [880], "branches": []}
# gained: {"lines": [880], "branches": []}

import pytest
from pypara.monetary import Price
from pypara.commons.numbers import Numeric

def test_scalar_subtract_not_implemented():
    class TestPrice(Price):
        def scalar_subtract(self, other: Numeric) -> 'Price':
            return super().scalar_subtract(other)
    
    test_price = TestPrice()
    with pytest.raises(NotImplementedError):
        test_price.scalar_subtract(10)
