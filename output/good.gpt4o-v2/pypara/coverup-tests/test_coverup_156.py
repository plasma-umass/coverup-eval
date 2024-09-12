# file: pypara/monetary.py:1375-1376
# asked: {"lines": [1375, 1376], "branches": []}
# gained: {"lines": [1375, 1376], "branches": []}

import pytest
from pypara.monetary import NonePrice, Price

def test_noneprice_lte():
    none_price = NonePrice()
    other_price = Price()  # Assuming Price can be instantiated like this

    assert none_price.lte(other_price) is True
