# file: pypara/monetary.py:1339-1340
# asked: {"lines": [1339, 1340], "branches": []}
# gained: {"lines": [1339, 1340], "branches": []}

import pytest
from pypara.monetary import NonePrice

def test_none_price_round():
    none_price = NonePrice()
    rounded_price = none_price.round(2)
    
    # Assert that the returned object is the same instance
    assert rounded_price is none_price

    # Assert that the type of the returned object is NonePrice
    assert isinstance(rounded_price, NonePrice)
