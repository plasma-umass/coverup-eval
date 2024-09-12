# file: pypara/monetary.py:665-666
# asked: {"lines": [665, 666], "branches": []}
# gained: {"lines": [665, 666], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import NoneMoney
from pypara.commons.numbers import Numeric

class TestNoneMoney:
    def test_multiply(self):
        none_money = NoneMoney()
        result = none_money.multiply(10)
        assert result is none_money

        result = none_money.multiply(Decimal('10.5'))
        assert result is none_money

        result = none_money.multiply(0)
        assert result is none_money

        result = none_money.multiply(-5)
        assert result is none_money
