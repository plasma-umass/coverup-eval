# file: pypara/monetary.py:468-471
# asked: {"lines": [470, 471], "branches": []}
# gained: {"lines": [470, 471], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomeMoney, Currency, Money
from datetime import date as Date

def test_scalar_add():
    currency = Currency('USD', 'US Dollar', 2, 'type', Decimal('0.01'), 'hashcache')
    some_money = SomeMoney(currency, Decimal('100.00'), Date(2023, 1, 1))
    
    result = some_money.scalar_add(50)
    
    assert result.ccy == currency
    assert result.qty == Decimal('150.00').quantize(currency.quantizer)
    assert result.dov == Date(2023, 1, 1)
