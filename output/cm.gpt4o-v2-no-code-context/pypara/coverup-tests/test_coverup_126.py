# file: pypara/monetary.py:155-166
# asked: {"lines": [166], "branches": []}
# gained: {"lines": [166], "branches": []}

import pytest
from pypara.monetary import Money

class TestMoney:
    def test_add_not_implemented(self):
        class ConcreteMoney(Money):
            def add(self, other: "Money") -> "Money":
                super().add(other)
        
        money_instance = ConcreteMoney()
        with pytest.raises(NotImplementedError):
            money_instance.add(money_instance)
