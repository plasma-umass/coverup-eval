# file pypara/monetary.py:1005-1011
# lines [1011]
# branches []

import pytest
from pypara.monetary import Price, Money

def test_price_money_not_implemented():
    class TestPrice(Price):
        pass

    test_price = TestPrice()
    
    with pytest.raises(NotImplementedError):
        _ = test_price.money
