# file: pypara/monetary.py:816-821
# asked: {"lines": [821], "branches": []}
# gained: {"lines": [821], "branches": []}

import pytest
from pypara.monetary import Price

def test_price_negative_not_implemented():
    class TestPrice(Price):
        pass

    test_price = TestPrice()
    
    with pytest.raises(NotImplementedError):
        test_price.negative()
