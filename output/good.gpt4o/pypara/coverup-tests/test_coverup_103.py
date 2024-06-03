# file pypara/monetary.py:1357-1358
# lines [1357, 1358]
# branches []

import pytest
from pypara.monetary import Price, NonePrice

def test_noneprice_scalar_subtract():
    none_price = NonePrice()
    result = none_price.scalar_subtract(10)
    assert result is none_price
