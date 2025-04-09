# file: pypara/monetary.py:1348-1349
# asked: {"lines": [1348, 1349], "branches": []}
# gained: {"lines": [1348, 1349], "branches": []}

import pytest
from pypara.monetary import Price, NonePrice

def test_none_price_add():
    none_price = NonePrice()
    other_price = Price()
    
    result = none_price.add(other_price)
    
    assert result is other_price
