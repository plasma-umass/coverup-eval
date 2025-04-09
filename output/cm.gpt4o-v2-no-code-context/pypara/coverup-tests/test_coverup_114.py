# file: pypara/monetary.py:1375-1376
# asked: {"lines": [1375, 1376], "branches": []}
# gained: {"lines": [1375, 1376], "branches": []}

import pytest
from pypara.monetary import Price, NonePrice

def test_noneprice_lte():
    none_price = NonePrice()
    other_price = Price()  # Assuming Price can be instantiated without arguments

    assert none_price.lte(other_price) is True

    another_none_price = NonePrice()
    assert none_price.lte(another_none_price) is True
