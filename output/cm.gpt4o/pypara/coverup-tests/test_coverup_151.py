# file pypara/monetary.py:1196-1202
# lines [1198, 1199, 1200, 1201, 1202]
# branches []

import pytest
from decimal import Decimal, InvalidOperation, DivisionByZero
from pypara.monetary import SomePrice, Currency, NoPrice
from datetime import date as Date

@pytest.fixture
def currency():
    return Currency(code='USD', name='United States Dollar', decimals=2, type='fiat', quantizer=Decimal('0.01'), hashcache=None)

def test_someprice_divide_invalid_operation(currency):
    qty = Decimal("100.00")
    dov = Date(2023, 1, 1)
    price = SomePrice(currency, qty, dov)
    
    result = price.divide("invalid")
    assert result == NoPrice

def test_someprice_divide_division_by_zero(currency):
    qty = Decimal("100.00")
    dov = Date(2023, 1, 1)
    price = SomePrice(currency, qty, dov)
    
    result = price.divide(0)
    assert result == NoPrice
