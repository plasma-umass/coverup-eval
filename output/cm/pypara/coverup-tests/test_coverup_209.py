# file pypara/monetary.py:88-98
# lines [98]
# branches []

import pytest
from pypara.monetary import Money
from typing import Any

class ConcreteMoney(Money):
    def is_equal(self, other: Any) -> bool:
        return super().is_equal(other)

def test_money_is_equal_not_implemented():
    concrete_money = ConcreteMoney()
    with pytest.raises(NotImplementedError):
        concrete_money.is_equal(None)
