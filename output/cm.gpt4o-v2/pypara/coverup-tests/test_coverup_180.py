# file: pypara/monetary.py:112-117
# asked: {"lines": [117], "branches": []}
# gained: {"lines": [117], "branches": []}

import pytest
from pypara.monetary import Money

def test_money_as_float_not_implemented():
    class TestMoney(Money):
        pass

    money_instance = TestMoney()
    with pytest.raises(NotImplementedError):
        money_instance.as_float()
