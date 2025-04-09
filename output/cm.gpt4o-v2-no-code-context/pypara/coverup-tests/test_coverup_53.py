# file: pypara/monetary.py:1192-1194
# asked: {"lines": [1192, 1193, 1194], "branches": []}
# gained: {"lines": [1192, 1193, 1194], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice, Currency, Date, SomeMoney

@pytest.fixture
def some_price():
    ccy = Currency('USD', 'Dollar', 2, 'USD', Decimal('0.01'), None)
    qty = Decimal('100.00')
    dov = Date(2023, 10, 1)
    return SomePrice(ccy, qty, dov)

def test_some_price_times(some_price):
    other = 2
    result = some_price.times(other)
    
    assert isinstance(result, SomeMoney)
    assert result.ccy == some_price.ccy
    assert result.qty == (some_price.qty * Decimal(other)).quantize(some_price.ccy.quantizer)
    assert result.dov == some_price.dov
