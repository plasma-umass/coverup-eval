# file pypara/monetary.py:1330-1331
# lines [1330, 1331]
# branches []

import pytest
from pypara.monetary import NonePrice

def test_none_price_abs():
    none_price = NonePrice()
    result = none_price.abs()
    assert result is none_price, "The result of abs() should be the same NonePrice instance"
