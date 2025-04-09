# file: pypara/monetary.py:656-657
# asked: {"lines": [656, 657], "branches": []}
# gained: {"lines": [656], "branches": []}

import pytest
from pypara.monetary import Money
from typing import Union

Numeric = Union[int, float]

class TestNoneMoney:
    def test_scalar_add(self):
        class NoneMoney(Money):
            def scalar_add(self, other: Numeric) -> "Money":
                return self

        none_money = NoneMoney()
        result = none_money.scalar_add(10)
        assert result is none_money
