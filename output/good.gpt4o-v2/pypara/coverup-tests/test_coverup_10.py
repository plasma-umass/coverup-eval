# file: pypara/monetary.py:1005-1011
# asked: {"lines": [1005, 1006, 1007, 1011], "branches": []}
# gained: {"lines": [1005, 1006, 1007, 1011], "branches": []}

import pytest
from pypara.monetary import Price, Money

def test_price_money_not_implemented():
    class TestPrice(Price):
        pass

    with pytest.raises(NotImplementedError):
        test_price = TestPrice()
        _ = test_price.money
