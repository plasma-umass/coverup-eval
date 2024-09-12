# file: pypara/monetary.py:802-807
# asked: {"lines": [802, 803, 807], "branches": []}
# gained: {"lines": [802, 803, 807], "branches": []}

import pytest
from pypara.monetary import Price

def test_price_as_integer_not_implemented():
    class TestPrice(Price):
        pass

    test_price = TestPrice()
    
    with pytest.raises(NotImplementedError):
        test_price.as_integer()
