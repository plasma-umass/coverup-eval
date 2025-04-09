# file: pypara/monetary.py:1339-1340
# asked: {"lines": [1339, 1340], "branches": []}
# gained: {"lines": [1339, 1340], "branches": []}

import pytest
from pypara.monetary import NonePrice

def test_noneprice_round():
    none_price = NonePrice()
    result = none_price.round()
    assert result is none_price

    result_with_digits = none_price.round(2)
    assert result_with_digits is none_price
