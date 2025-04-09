# file pypara/monetary.py:410-420
# lines [410, 411, 415, 417, 419]
# branches []

import pytest
from decimal import Decimal
from datetime import date
from pypara.monetary import SomeMoney

class Currency:
    def __init__(self, code, name, decimals, type, quantizer, hashcache):
        self.code = code
        self.name = name
        self.decimals = decimals
        self.type = type
        self.quantizer = quantizer
        self.hashcache = hashcache

@pytest.fixture
def mock_currency(mocker):
    return Currency('USD', 'US Dollar', 2, 'fiat', Decimal('0.01'), True)

def test_some_money_defined_and_undefined(mock_currency):
    quantity = Decimal('100.00')
    date_of_value = date.today()
    
    money = SomeMoney(ccy=mock_currency, qty=quantity, dov=date_of_value)
    
    assert money.defined is True
    assert money.undefined is False
    assert money.ccy == mock_currency
    assert money.qty == quantity
    assert money.dov == date_of_value
