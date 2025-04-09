# file: pypara/monetary.py:177-188
# asked: {"lines": [188], "branches": []}
# gained: {"lines": [188], "branches": []}

import pytest
from pypara.monetary import Money

def test_money_subtract_not_implemented():
    class TestMoney(Money):
        def subtract(self, other: "Money") -> "Money":
            super().subtract(other)
    
    money_instance = TestMoney()
    with pytest.raises(NotImplementedError):
        money_instance.subtract(money_instance)
