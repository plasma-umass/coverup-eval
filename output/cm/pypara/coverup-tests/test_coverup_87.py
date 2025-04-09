# file pypara/monetary.py:795-800
# lines [795, 796, 800]
# branches []

import pytest
from pypara.monetary import Price

def test_price_as_float_not_implemented():
    class TestPrice(Price):
        pass

    price = TestPrice()
    with pytest.raises(NotImplementedError):
        price.as_float()
