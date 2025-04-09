# file: pypara/monetary.py:509-515
# asked: {"lines": [509, 511, 512, 513, 514, 515], "branches": []}
# gained: {"lines": [509, 511, 512, 513, 514, 515], "branches": []}

import pytest
from decimal import Decimal, InvalidOperation, DivisionByZero
from pypara.monetary import SomeMoney, NoMoney, Currency, Date

def test_floor_divide_valid():
    currency = Currency('USD', '2', 2, 'standard', Decimal('0.01'), None)
    quantity = Decimal('100.00')
    date = Date(2023, 10, 1)
    money = SomeMoney(currency, quantity, date)
    
    result = money.floor_divide(3)
    
    assert isinstance(result, SomeMoney)
    assert result.ccy == currency
    assert result.qty == Decimal('33.00')
    assert result.dov == date

def test_floor_divide_invalid_operation():
    currency = Currency('USD', '2', 2, 'standard', Decimal('0.01'), None)
    quantity = Decimal('100.00')
    date = Date(2023, 10, 1)
    money = SomeMoney(currency, quantity, date)
    
    result = money.floor_divide('invalid')
    
    assert result == NoMoney

def test_floor_divide_division_by_zero():
    currency = Currency('USD', '2', 2, 'standard', Decimal('0.01'), None)
    quantity = Decimal('100.00')
    date = Date(2023, 10, 1)
    money = SomeMoney(currency, quantity, date)
    
    result = money.floor_divide(0)
    
    assert result == NoMoney
