# file: pypara/monetary.py:671-672
# asked: {"lines": [671, 672], "branches": []}
# gained: {"lines": [671], "branches": []}

import pytest
from pypara.monetary import Money

class TestNoneMoney:
    def test_floor_divide(self):
        class NoneMoney(Money):
            def floor_divide(self, other) -> "Money":
                return self

        none_money_instance = NoneMoney()
        result = none_money_instance.floor_divide(10)
        
        assert result is none_money_instance
