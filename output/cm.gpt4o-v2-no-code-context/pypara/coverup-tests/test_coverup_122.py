# file: pypara/monetary.py:140-145
# asked: {"lines": [145], "branches": []}
# gained: {"lines": [145], "branches": []}

import pytest
from pypara.monetary import Money

class TestMoney:
    def test_positive_not_implemented(self):
        class TestMoneySubclass(Money):
            pass

        with pytest.raises(NotImplementedError):
            TestMoneySubclass().positive()
