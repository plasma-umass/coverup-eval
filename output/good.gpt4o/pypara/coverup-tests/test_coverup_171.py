# file pypara/monetary.py:1034-1036
# lines [1036]
# branches []

import pytest
from pypara.monetary import Price

def test_price_float_abstract_method():
    with pytest.raises(TypeError):
        class TestPrice(Price):
            pass

        test_price = TestPrice()
        float(test_price)
