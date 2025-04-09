# file: pypara/monetary.py:155-166
# asked: {"lines": [166], "branches": []}
# gained: {"lines": [166], "branches": []}

import pytest
from pypara.monetary import Money

def test_money_add_not_implemented():
    class TestMoney(Money):
        def add(self, other: "Money") -> "Money":
            return super().add(other)
    
    money_instance = TestMoney()
    with pytest.raises(NotImplementedError):
        money_instance.add(money_instance)
