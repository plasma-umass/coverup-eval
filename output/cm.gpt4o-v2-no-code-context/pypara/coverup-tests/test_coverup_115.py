# file: pypara/monetary.py:1372-1373
# asked: {"lines": [1372, 1373], "branches": []}
# gained: {"lines": [1372, 1373], "branches": []}

import pytest
from pypara.monetary import Price, NonePrice

class MockPrice(Price):
    def __init__(self, defined):
        self.defined = defined

def test_noneprice_lt():
    none_price = NonePrice()
    
    other_price_true = MockPrice(defined=True)
    assert none_price.lt(other_price_true) == True
    
    other_price_false = MockPrice(defined=False)
    assert none_price.lt(other_price_false) == False
