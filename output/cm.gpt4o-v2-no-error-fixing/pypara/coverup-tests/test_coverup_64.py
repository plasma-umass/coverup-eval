# file: pypara/monetary.py:1357-1358
# asked: {"lines": [1357, 1358], "branches": []}
# gained: {"lines": [1357, 1358], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import NonePrice
from pypara.commons.numbers import Numeric

def test_none_price_scalar_subtract():
    none_price = NonePrice()
    result = none_price.scalar_subtract(Decimal('10.0'))
    assert result is none_price
