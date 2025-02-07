# file: pypara/monetary.py:823-828
# asked: {"lines": [823, 824, 828], "branches": []}
# gained: {"lines": [823, 824, 828], "branches": []}

import pytest
from pypara.monetary import Price

def test_price_positive_not_implemented():
    class TestPrice(Price):
        def __init__(self, value):
            self.value = value

    test_price = TestPrice(100)
    
    with pytest.raises(NotImplementedError):
        test_price.positive()
