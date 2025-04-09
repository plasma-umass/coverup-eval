# file pypara/monetary.py:208-215
# lines [215]
# branches []

import pytest
from pypara.monetary import Money

def test_money_divide_not_implemented():
    class TestMoney(Money):
        pass

    test_money = TestMoney()
    
    with pytest.raises(NotImplementedError):
        test_money.divide(1)
