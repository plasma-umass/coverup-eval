# file pypara/monetary.py:671-672
# lines [671, 672]
# branches []

import pytest
from pypara.monetary import Money
from typing import Union

Numeric = Union[int, float]

class TestNoneMoney:
    def test_floor_divide(self):
        class NoneMoney(Money):
            def floor_divide(self, other: Numeric) -> "Money":
                return self

        none_money = NoneMoney()
        result = none_money.floor_divide(10)
        assert result is none_money
