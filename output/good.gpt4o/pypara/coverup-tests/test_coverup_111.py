# file pypara/monetary.py:1381-1382
# lines [1381, 1382]
# branches []

import pytest
from pypara.monetary import Price, NonePrice

def test_noneprice_gte():
    class MockPrice(Price):
        def __init__(self, undefined):
            self.undefined = undefined

    none_price = NonePrice()
    other_price = MockPrice(undefined=True)
    
    assert none_price.gte(other_price) == True

    other_price = MockPrice(undefined=False)
    
    assert none_price.gte(other_price) == False
