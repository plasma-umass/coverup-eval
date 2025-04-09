# file: pypara/monetary.py:662-663
# asked: {"lines": [662, 663], "branches": []}
# gained: {"lines": [662], "branches": []}

import pytest
from pypara.monetary import Money
from typing import Union

Numeric = Union[int, float]

class TestNoneMoney:
    def test_scalar_subtract(self):
        class NoneMoney(Money):
            def scalar_subtract(self, other: Numeric) -> "Money":
                return self

        none_money = NoneMoney()
        result = none_money.scalar_subtract(10)
        assert result is none_money
