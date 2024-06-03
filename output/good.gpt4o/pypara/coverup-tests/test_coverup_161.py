# file pypara/monetary.py:816-821
# lines [821]
# branches []

import pytest
from pypara.monetary import Price

def test_price_negative_not_implemented():
    class TestPrice(Price):
        pass

    test_price_instance = TestPrice()
    
    with pytest.raises(NotImplementedError):
        test_price_instance.negative()
