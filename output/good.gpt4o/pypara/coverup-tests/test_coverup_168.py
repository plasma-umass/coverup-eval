# file pypara/monetary.py:809-814
# lines [814]
# branches []

import pytest
from pypara.monetary import Price

def test_price_abs_not_implemented():
    class TestPrice(Price):
        pass

    test_price = TestPrice()
    
    with pytest.raises(NotImplementedError):
        test_price.abs()
