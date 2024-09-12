# file: pypara/monetary.py:671-672
# asked: {"lines": [671, 672], "branches": []}
# gained: {"lines": [671, 672], "branches": []}

import pytest
from pypara.monetary import NoneMoney, Money

class TestNoneMoney:
    def test_floor_divide(self):
        none_money = NoneMoney()
        result = none_money.floor_divide(10)
        assert result is none_money
