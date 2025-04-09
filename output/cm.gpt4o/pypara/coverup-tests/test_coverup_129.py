# file pypara/monetary.py:88-98
# lines [98]
# branches []

import pytest
from pypara.monetary import Money

def test_money_is_equal_not_implemented():
    class TestMoney(Money):
        pass

    test_money = TestMoney()
    
    with pytest.raises(NotImplementedError):
        test_money.is_equal(None)
