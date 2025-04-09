# file: pypara/monetary.py:140-145
# asked: {"lines": [145], "branches": []}
# gained: {"lines": [145], "branches": []}

import pytest
from pypara.monetary import Money

def test_money_positive_not_implemented():
    class TestMoney(Money):
        pass

    money_instance = TestMoney()
    with pytest.raises(NotImplementedError):
        money_instance.positive()
