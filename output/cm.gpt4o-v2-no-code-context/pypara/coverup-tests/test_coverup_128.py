# file: pypara/monetary.py:208-215
# asked: {"lines": [215], "branches": []}
# gained: {"lines": [215], "branches": []}

import pytest
from pypara.monetary import Money

class TestMoney:
    def test_divide_not_implemented(self):
        class ConcreteMoney(Money):
            def divide(self, other) -> "Money":
                super().divide(other)
        
        money_instance = ConcreteMoney()
        with pytest.raises(NotImplementedError):
            money_instance.divide(10)
