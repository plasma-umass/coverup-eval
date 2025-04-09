# file: pypara/monetary.py:1342-1343
# asked: {"lines": [1342, 1343], "branches": []}
# gained: {"lines": [1342, 1343], "branches": []}

import pytest
from pypara.monetary import NonePrice

def test_noneprice_negative():
    none_price = NonePrice()
    result = none_price.negative()
    assert result is none_price
