# file: pypara/monetary.py:1369-1370
# asked: {"lines": [1369, 1370], "branches": []}
# gained: {"lines": [1369, 1370], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import NonePrice

def test_noneprice_floor_divide():
    none_price = NonePrice()
    other = Decimal(10)  # Using Decimal as a valid Numeric type
    result = none_price.floor_divide(other)
    
    assert result is none_price  # Ensure the method returns self

