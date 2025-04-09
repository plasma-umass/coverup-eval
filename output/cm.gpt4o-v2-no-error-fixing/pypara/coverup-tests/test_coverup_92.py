# file: pypara/monetary.py:1366-1367
# asked: {"lines": [1367], "branches": []}
# gained: {"lines": [1367], "branches": []}

import pytest
from pypara.monetary import NonePrice
from pypara.commons.numbers import Numeric

def test_noneprice_divide():
    none_price = NonePrice()
    result = none_price.divide(10)
    assert result is none_price
