# file: pypara/monetary.py:802-807
# asked: {"lines": [807], "branches": []}
# gained: {"lines": [807], "branches": []}

import pytest
from pypara.monetary import Price, MonetaryOperationException

def test_price_as_integer_not_implemented():
    class TestPrice(Price):
        pass

    test_price = TestPrice()
    
    with pytest.raises(NotImplementedError):
        test_price.as_integer()
