# file pypara/monetary.py:509-515
# lines [509, 511, 512, 513, 514, 515]
# branches []

import pytest
from decimal import Decimal, InvalidOperation, DivisionByZero
from pypara.monetary import SomeMoney, NoMoney, Currency, Money
from datetime import date as Date

def test_some_money_floor_divide():
    currency = Currency('USD', 'US Dollar', 2, Decimal('0.01'), Decimal('0.01'), None)
    some_money = SomeMoney(currency, Decimal('100.00'), Date(2023, 1, 1))

    # Test normal floor division
    result = some_money.floor_divide(2)
    assert result == SomeMoney(currency, Decimal('50.00').quantize(currency.quantizer), Date(2023, 1, 1))

    # Test floor division by zero
    result = some_money.floor_divide(0)
    assert result == NoMoney

    # Test floor division with invalid operation
    result = some_money.floor_divide('invalid')
    assert result == NoMoney
