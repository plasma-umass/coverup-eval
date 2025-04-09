# file pypara/monetary.py:891-898
# lines [898]
# branches []

import pytest
from pypara.monetary import Price, Numeric

class IncompletePrice(Price):
    pass

def test_price_times_not_implemented():
    incomplete_price = IncompletePrice()
    with pytest.raises(NotImplementedError):
        incomplete_price.times(10)
