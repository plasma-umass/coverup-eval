# file: pypara/monetary.py:199-206
# asked: {"lines": [206], "branches": []}
# gained: {"lines": [206], "branches": []}

import pytest
from pypara.monetary import Money

class TestMoney:
    def test_multiply_not_implemented(self):
        class ConcreteMoney(Money):
            def multiply(self, other):
                super().multiply(other)
        
        money_instance = ConcreteMoney()
        with pytest.raises(NotImplementedError):
            money_instance.multiply(10)
