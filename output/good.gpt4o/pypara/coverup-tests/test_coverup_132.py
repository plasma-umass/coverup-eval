# file pypara/monetary.py:119-124
# lines [124]
# branches []

import pytest
from pypara.monetary import Money, MonetaryOperationException

def test_money_as_integer_not_implemented():
    class TestMoney(Money):
        pass

    test_money_instance = TestMoney()
    
    with pytest.raises(NotImplementedError):
        test_money_instance.as_integer()
