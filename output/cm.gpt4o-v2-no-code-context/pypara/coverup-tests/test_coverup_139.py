# file: pypara/monetary.py:795-800
# asked: {"lines": [800], "branches": []}
# gained: {"lines": [800], "branches": []}

import pytest
from pypara.monetary import Price, MonetaryOperationException

def test_price_as_float_not_implemented():
    class TestPrice(Price):
        pass

    test_price = TestPrice()
    
    with pytest.raises(NotImplementedError):
        test_price.as_float()
