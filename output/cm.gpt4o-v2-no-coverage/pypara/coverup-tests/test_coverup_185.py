# file: pypara/monetary.py:671-672
# asked: {"lines": [672], "branches": []}
# gained: {"lines": [672], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import NoneMoney
from pypara.commons.numbers import Numeric

class TestNoneMoney:
    def test_floor_divide(self):
        # Create an instance of NoneMoney
        none_money = NoneMoney()

        # Test floor_divide with an integer
        result = none_money.floor_divide(10)
        assert result is none_money

        # Test floor_divide with a float
        result = none_money.floor_divide(10.5)
        assert result is none_money

        # Test floor_divide with a Decimal
        result = none_money.floor_divide(Decimal('10.5'))
        assert result is none_money

        # Test floor_divide with a custom Numeric type (Amount or Quantity)
        class Amount:
            pass

        amount = Amount()
        result = none_money.floor_divide(amount)
        assert result is none_money

        class Quantity:
            pass

        quantity = Quantity()
        result = none_money.floor_divide(quantity)
        assert result is none_money
