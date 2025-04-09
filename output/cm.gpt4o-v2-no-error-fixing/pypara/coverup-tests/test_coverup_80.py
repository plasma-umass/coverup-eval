# file: pypara/monetary.py:119-124
# asked: {"lines": [124], "branches": []}
# gained: {"lines": [124], "branches": []}

import pytest
from pypara.monetary import Money

def test_money_as_integer_not_implemented():
    class TestMoney(Money):
        pass

    money_instance = TestMoney()
    with pytest.raises(NotImplementedError):
        money_instance.as_integer()
