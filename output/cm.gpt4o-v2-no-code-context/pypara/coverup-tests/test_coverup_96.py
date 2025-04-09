# file: pypara/monetary.py:1360-1361
# asked: {"lines": [1360, 1361], "branches": []}
# gained: {"lines": [1360, 1361], "branches": []}

import pytest
from pypara.monetary import Price, NonePrice

def test_noneprice_multiply():
    none_price = NonePrice()
    result = none_price.multiply(10)
    assert result is none_price
