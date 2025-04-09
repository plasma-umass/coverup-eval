# file: pypara/monetary.py:88-98
# asked: {"lines": [98], "branches": []}
# gained: {"lines": [98], "branches": []}

import pytest
from pypara.monetary import Money

class TestMoney:
    def test_is_equal_not_implemented(self):
        class DummyMoney(Money):
            pass

        dummy_money = DummyMoney()
        with pytest.raises(NotImplementedError):
            dummy_money.is_equal(None)
