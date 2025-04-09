# file: pypara/monetary.py:1330-1331
# asked: {"lines": [1330, 1331], "branches": []}
# gained: {"lines": [1330, 1331], "branches": []}

import pytest
from pypara.monetary import Price, NonePrice

def test_none_price_abs():
    none_price = NonePrice()
    result = none_price.abs()
    assert result is none_price
