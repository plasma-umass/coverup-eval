# file pypara/monetary.py:112-117
# lines [112, 113, 117]
# branches []

import pytest
from pypara.monetary import Money

def test_money_as_float_not_implemented():
    class TestMoney(Money):
        pass

    money = TestMoney()
    with pytest.raises(NotImplementedError):
        money.as_float()
