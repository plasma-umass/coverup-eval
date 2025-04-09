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
        result = none_money.scalar_subtract(10)
        assert result is none_money

    def test_scalar_subtract_with_decimal(self):
        none_money = NoneMoney()
        result = none_money.scalar_subtract(Decimal('10.5'))
        assert result is none_money

    def test_scalar_subtract_with_float(self):
        none_money = NoneMoney()
        result = none_money.scalar_subtract(10.5)
        assert result is none_money

    def test_scalar_subtract_with_int(self):
        none_money = NoneMoney()
        result = none_money.scalar_subtract(10)
        assert result is none_money

    def test_scalar_subtract_with_amount(self, mocker):
        Amount = mocker.patch('pypara.commons.numbers.Amount', autospec=True)
        amount_instance = Amount.return_value
        none_money = NoneMoney()
        result = none_money.scalar_subtract(amount_instance)
        assert result is none_money

    def test_scalar_subtract_with_quantity(self, mocker):
        Quantity = mocker.patch('pypara.commons.numbers.Quantity', autospec=True)
        quantity_instance = Quantity.return_value
        none_money = NoneMoney()
        result = none_money.scalar_subtract(quantity_instance)
        assert result is none_money
