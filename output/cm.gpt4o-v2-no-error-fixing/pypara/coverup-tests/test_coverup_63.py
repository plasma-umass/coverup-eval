# file: pypara/monetary.py:1348-1349
# asked: {"lines": [1348, 1349], "branches": []}
# gained: {"lines": [1348, 1349], "branches": []}

import pytest
from pypara.monetary import NonePrice, Price

def test_none_price_add():
    none_price = NonePrice()
    other_price = Price()  # Assuming Price can be instantiated like this

    result = none_price.add(other_price)

    assert result is other_price
