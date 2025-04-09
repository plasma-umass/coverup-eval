# file pypara/monetary.py:147-153
# lines [153]
# branches []

import pytest
from pypara.monetary import Money

def test_money_round_not_implemented():
    class TestMoney(Money):
        pass

    test_money = TestMoney()
    
    with pytest.raises(NotImplementedError):
        test_money.round()
