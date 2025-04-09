# file pypara/monetary.py:771-781
# lines [781]
# branches []

import pytest
from pypara.monetary import Price

def test_price_is_equal_not_implemented():
    class TestPrice(Price):
        pass

    test_price = TestPrice()
    
    with pytest.raises(NotImplementedError):
        test_price.is_equal(None)
