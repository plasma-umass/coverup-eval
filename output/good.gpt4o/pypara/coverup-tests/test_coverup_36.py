# file pypara/monetary.py:140-145
# lines [140, 141, 145]
# branches []

import pytest
from pypara.monetary import Money

def test_money_positive_not_implemented():
    class TestMoney(Money):
        pass

    test_money_instance = TestMoney()
    
    with pytest.raises(NotImplementedError):
        test_money_instance.positive()
