# file: pypara/monetary.py:656-657
# asked: {"lines": [656, 657], "branches": []}
# gained: {"lines": [656, 657], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import NoneMoney
from pypara.commons.numbers import Numeric

class TestNoneMoney:
    def test_scalar_add(self):
        none_money = NoneMoney()
        result = none_money.scalar_add(10)
        assert result is none_money

        result = none_money.scalar_add(Decimal('10.5'))
        assert result is none_money

        result = none_money.scalar_add(0)
        assert result is none_money

        result = none_money.scalar_add(-5)
        assert result is none_money

        result = none_money.scalar_add(Decimal('-5.5'))
        assert result is none_money
