# file: pypara/monetary.py:1369-1370
# asked: {"lines": [1370], "branches": []}
# gained: {"lines": [1370], "branches": []}

import pytest
from pypara.monetary import NonePrice
from pypara.commons.numbers import Numeric

def test_none_price_floor_divide():
    none_price = NonePrice()
    other = 10  # Example numeric value
    result = none_price.floor_divide(other)
    assert result is none_price
