# file: pypara/monetary.py:823-828
# asked: {"lines": [828], "branches": []}
# gained: {"lines": [828], "branches": []}

import pytest
from pypara.monetary import Price

def test_price_positive_not_implemented():
    class TestPrice(Price):
        pass

    test_price = TestPrice()
    with pytest.raises(NotImplementedError):
        test_price.positive()
