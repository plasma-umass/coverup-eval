# file: pypara/monetary.py:509-515
# asked: {"lines": [509, 511, 512, 513, 514, 515], "branches": []}
# gained: {"lines": [509, 511, 512, 513, 514, 515], "branches": []}

import pytest
from decimal import Decimal, DivisionByZero, InvalidOperation
from pypara.monetary import SomeMoney, NoMoney
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

def test_floor_divide_valid():
    currency = Currency.of('USD', 'US Dollar', 2, CurrencyType.MONEY)
    some_money = SomeMoney(currency, Decimal('100.00'), Date(2023, 10, 1))
    result = some_money.floor_divide(3)
    assert result == SomeMoney(currency, Decimal('33.00').quantize(currency.quantizer), Date(2023, 10, 1))

def test_floor_divide_invalid_operation():
    currency = Currency.of('USD', 'US Dollar', 2, CurrencyType.MONEY)
    some_money = SomeMoney(currency, Decimal('100.00'), Date(2023, 10, 1))
    result = some_money.floor_divide('invalid')
    assert result == NoMoney

def test_floor_divide_division_by_zero():
    currency = Currency.of('USD', 'US Dollar', 2, CurrencyType.MONEY)
    some_money = SomeMoney(currency, Decimal('100.00'), Date(2023, 10, 1))
    result = some_money.floor_divide(0)
    assert result == NoMoney
