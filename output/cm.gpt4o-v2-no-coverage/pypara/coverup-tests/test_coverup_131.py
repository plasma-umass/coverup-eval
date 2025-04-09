# file: pypara/monetary.py:1330-1331
# asked: {"lines": [1330, 1331], "branches": []}
# gained: {"lines": [1330, 1331], "branches": []}

import pytest
from pypara.monetary import NonePrice

def test_noneprice_abs():
    none_price = NonePrice()
    result = none_price.abs()
    assert result is none_price
