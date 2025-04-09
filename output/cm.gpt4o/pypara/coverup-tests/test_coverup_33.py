# file pypara/monetary.py:133-138
# lines [133, 134, 138]
# branches []

import pytest
from pypara.monetary import Money

def test_money_negative_not_implemented():
    class TestMoney(Money):
        pass

    test_money = TestMoney()
    
    with pytest.raises(NotImplementedError):
        test_money.negative()
