# file: pypara/monetary.py:1369-1370
# asked: {"lines": [1369, 1370], "branches": []}
# gained: {"lines": [1369, 1370], "branches": []}

import pytest
from pypara.monetary import Price, NonePrice

def test_none_price_floor_divide():
    none_price = NonePrice()
    result = none_price.floor_divide(10)
    assert result is none_price
