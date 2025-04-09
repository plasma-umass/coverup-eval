# file: pypara/monetary.py:177-188
# asked: {"lines": [188], "branches": []}
# gained: {"lines": [188], "branches": []}

import pytest
from pypara.monetary import Money

def test_money_subtract_not_implemented():
    class TestMoney(Money):
        def subtract(self, other: "Money") -> "Money":
            super().subtract(other)
    
    test_money = TestMoney()
    with pytest.raises(NotImplementedError):
        test_money.subtract(test_money)
