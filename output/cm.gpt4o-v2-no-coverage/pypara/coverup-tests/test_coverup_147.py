# file: pypara/monetary.py:668-669
# asked: {"lines": [668, 669], "branches": []}
# gained: {"lines": [668, 669], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import NoneMoney
from pypara.commons.numbers import Numeric

class TestNoneMoney:
    def test_divide(self):
        none_money = NoneMoney()
        result = none_money.divide(10)
        assert result is none_money

    def test_divide_with_decimal(self):
        none_money = NoneMoney()
        result = none_money.divide(Decimal('10.5'))
        assert result is none_money

    def test_divide_with_float(self):
        none_money = NoneMoney()
        result = none_money.divide(10.5)
        assert result is none_money

    def test_divide_with_int(self):
        none_money = NoneMoney()
        result = none_money.divide(10)
        assert result is none_money

    def test_divide_with_amount(self, mocker):
        Amount = mocker.patch('pypara.commons.numbers.Amount', autospec=True)
        amount_instance = Amount.return_value
        none_money = NoneMoney()
        result = none_money.divide(amount_instance)
        assert result is none_money

    def test_divide_with_quantity(self, mocker):
        Quantity = mocker.patch('pypara.commons.numbers.Quantity', autospec=True)
        quantity_instance = Quantity.return_value
        none_money = NoneMoney()
        result = none_money.divide(quantity_instance)
        assert result is none_money
