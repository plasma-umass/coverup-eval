# file: pypara/monetary.py:662-663
# asked: {"lines": [662, 663], "branches": []}
# gained: {"lines": [662, 663], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import NoneMoney
from pypara.commons.numbers import Numeric

class TestNoneMoney:
    def test_scalar_subtract(self):
        none_money = NoneMoney()
        result = none_money.scalar_subtract(Decimal('10.00'))
        assert result is none_money
