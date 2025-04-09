# file: pypara/monetary.py:671-672
# asked: {"lines": [671, 672], "branches": []}
# gained: {"lines": [671, 672], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import NoneMoney
from pypara.commons.numbers import Numeric

class TestNoneMoney:
    def test_floor_divide(self):
        none_money = NoneMoney()
        result = none_money.floor_divide(10)
        assert result is none_money

        result = none_money.floor_divide(Decimal('10.5'))
        assert result is none_money

        result = none_money.floor_divide(0)
        assert result is none_money

        result = none_money.floor_divide(-5)
        assert result is none_money
