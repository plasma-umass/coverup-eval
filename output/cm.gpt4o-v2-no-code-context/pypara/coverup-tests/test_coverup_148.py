# file: pypara/monetary.py:1387-1388
# asked: {"lines": [1388], "branches": []}
# gained: {"lines": [1388], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import NonePrice

def test_none_price_with_qty():
    none_price = NonePrice()
    qty = Decimal('10.00')
    
    result = none_price.with_qty(qty)
    
    assert result is none_price
