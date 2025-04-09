# file pypara/monetary.py:1278-1281
# lines [1278, 1279, 1280, 1281]
# branches []

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import Currency, Money, Price, SomeMoney, SomePrice

def test_someprice_money():
    # Arrange
    ccy = Currency('USD', 'US Dollar', 2, 'type', Decimal('0.01'), 'hashcache')
    qty = Decimal('123.45')
    dov = Date(2023, 10, 1)
    some_price = SomePrice(ccy, qty, dov)
    
    # Act
    money = some_price.money
    
    # Assert
    assert isinstance(money, SomeMoney)
    assert money.ccy == ccy
    assert money.qty == qty.quantize(ccy.quantizer)
    assert money.dov == dov
