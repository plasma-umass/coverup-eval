# file: pypara/monetary.py:802-807
# asked: {"lines": [807], "branches": []}
# gained: {"lines": [807], "branches": []}

import pytest
from pypara.monetary import Price

def test_price_as_integer_not_implemented():
    class TestPrice(Price):
        pass

    price = TestPrice()
    with pytest.raises(NotImplementedError):
        price.as_integer()
