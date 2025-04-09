# file: pypara/monetary.py:1204-1210
# asked: {"lines": [1204, 1206, 1207, 1208, 1209, 1210], "branches": []}
# gained: {"lines": [1204, 1206, 1207, 1208, 1209, 1210], "branches": []}

import pytest
from decimal import Decimal, InvalidOperation, DivisionByZero
from pypara.monetary import SomePrice, NoPrice, Currency, Date

@pytest.fixture
def currency():
    return Currency(code="USD", name="US Dollar", decimals=2, type="fiat", quantizer=Decimal("0.01"), hashcache=None)

@pytest.fixture
def date():
    return Date(2023, 10, 1)

def test_someprice_floor_divide_valid(currency, date):
    qty = Decimal("100.00")
    price = SomePrice(currency, qty, date)
    
    result = price.floor_divide(2)
    
    assert isinstance(result, SomePrice)
    assert result.ccy == currency
    assert result.qty == Decimal("50")
    assert result.dov == date

def test_someprice_floor_divide_invalid_operation(currency, date):
    qty = Decimal("100.00")
    price = SomePrice(currency, qty, date)
    
    result = price.floor_divide("invalid")
    
    assert result == NoPrice

def test_someprice_floor_divide_division_by_zero(currency, date):
    qty = Decimal("100.00")
    price = SomePrice(currency, qty, date)
    
    result = price.floor_divide(0)
    
    assert result == NoPrice
