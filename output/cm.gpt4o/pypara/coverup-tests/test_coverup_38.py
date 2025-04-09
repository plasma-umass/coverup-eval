# file pypara/monetary.py:199-206
# lines [199, 200, 206]
# branches []

import pytest
from pypara.monetary import Money
from abc import ABC, abstractmethod

class TestMoney:
    def test_multiply_not_implemented(self):
        class ConcreteMoney(Money, ABC):
            pass

        money_instance = ConcreteMoney()
        with pytest.raises(NotImplementedError):
            money_instance.multiply(10)
