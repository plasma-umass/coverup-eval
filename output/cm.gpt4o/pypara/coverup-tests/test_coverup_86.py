# file pypara/monetary.py:656-657
# lines [656, 657]
# branches []

import pytest
from pypara.monetary import Money

class NoneMoney(Money):
    def scalar_add(self, other: "Numeric") -> "Money":
        return self

def test_none_money_scalar_add():
    none_money = NoneMoney()
    result = none_money.scalar_add(100)
    assert result is none_money
