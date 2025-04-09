# file: pypara/monetary.py:501-507
# asked: {"lines": [503, 504, 505, 506, 507], "branches": []}
# gained: {"lines": [503, 504, 505, 506, 507], "branches": []}

import pytest
from decimal import Decimal, InvalidOperation, DivisionByZero
from pypara.monetary import SomeMoney, NoMoney, Currency, Date

def test_some_money_divide_success():
    currency = Currency('USD', 'US Dollar', 2, 'CURRENCY', Decimal('0.01'), None)
    quantity = Decimal('100.00')
    date = Date(2023, 10, 1)
    some_money = SomeMoney(currency, quantity, date)
    
    result = some_money.divide(2)
    
    assert result.ccy == currency
    assert result.qty == Decimal('50.00').quantize(currency.quantizer)
    assert result.dov == date

def test_some_money_divide_invalid_operation():
    currency = Currency('USD', 'US Dollar', 2, 'CURRENCY', Decimal('0.01'), None)
    quantity = Decimal('100.00')
    date = Date(2023, 10, 1)
    some_money = SomeMoney(currency, quantity, date)
    
    result = some_money.divide('invalid')
    
    assert result == NoMoney

def test_some_money_divide_division_by_zero():
    currency = Currency('USD', 'US Dollar', 2, 'CURRENCY', Decimal('0.01'), None)
    quantity = Decimal('100.00')
    date = Date(2023, 10, 1)
    some_money = SomeMoney(currency, quantity, date)
    
    result = some_money.divide(0)
    
    assert result == NoMoney
