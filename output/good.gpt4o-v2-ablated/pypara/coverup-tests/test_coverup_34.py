# file: pypara/monetary.py:1339-1340
# asked: {"lines": [1339, 1340], "branches": []}
# gained: {"lines": [1339, 1340], "branches": []}

import pytest
from pypara.monetary import NonePrice, Price

def test_none_price_round():
    none_price = NonePrice()
    rounded_price = none_price.round(2)
    
    assert rounded_price is none_price

