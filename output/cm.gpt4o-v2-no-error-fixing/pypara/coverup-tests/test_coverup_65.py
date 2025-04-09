# file: pypara/monetary.py:1351-1352
# asked: {"lines": [1351, 1352], "branches": []}
# gained: {"lines": [1351, 1352], "branches": []}

import pytest
from pypara.monetary import NonePrice
from pypara.commons.numbers import Numeric

def test_noneprice_scalar_add():
    none_price = NonePrice()
    result = none_price.scalar_add(10)  # Using an arbitrary numeric value
    assert result is none_price  # Ensure the method returns the instance itself
