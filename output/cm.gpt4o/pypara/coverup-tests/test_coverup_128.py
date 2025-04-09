# file pypara/monetary.py:112-117
# lines [117]
# branches []

import pytest
from pypara.monetary import Money, MonetaryOperationException

def test_money_as_float_not_implemented():
    class TestMoney(Money):
        pass

    test_money_instance = TestMoney()
    
    with pytest.raises(NotImplementedError):
        test_money_instance.as_float()
