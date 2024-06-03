# file pypara/monetary.py:1339-1340
# lines [1339, 1340]
# branches []

import pytest
from pypara.monetary import Price, NonePrice

def test_none_price_round():
    none_price = NonePrice()
    rounded_price = none_price.round(2)
    
    assert rounded_price is none_price
