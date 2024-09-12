# file: pypara/monetary.py:1354-1355
# asked: {"lines": [1354, 1355], "branches": []}
# gained: {"lines": [1354, 1355], "branches": []}

import pytest
from pypara.monetary import NonePrice, Price

def test_none_price_subtract():
    none_price = NonePrice()
    other_price = Price()

    result = none_price.subtract(other_price)

    assert result == -other_price
