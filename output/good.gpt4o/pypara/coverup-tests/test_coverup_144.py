# file pypara/monetary.py:322-328
# lines [328]
# branches []

import pytest
from pypara.monetary import Money

def test_money_price_not_implemented():
    class TestMoney(Money):
        pass

    test_money = TestMoney()
    with pytest.raises(NotImplementedError):
        _ = test_money.price
