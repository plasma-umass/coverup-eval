# file: pypara/monetary.py:891-898
# asked: {"lines": [898], "branches": []}
# gained: {"lines": [898], "branches": []}

import pytest
from pypara.monetary import Price
from pypara.commons.numbers import Numeric

def test_price_times_not_implemented():
    class TestPrice(Price):
        def times(self, other: Numeric) -> "Money":
            super().times(other)
    
    price = TestPrice()
    with pytest.raises(NotImplementedError):
        price.times(10)
