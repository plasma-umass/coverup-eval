# file: pypara/monetary.py:1378-1379
# asked: {"lines": [1378, 1379], "branches": []}
# gained: {"lines": [1378, 1379], "branches": []}

import pytest
from pypara.monetary import NonePrice, Price

class MockPrice(Price):
    def __init__(self, value):
        self.value = value

def test_noneprice_gt():
    none_price = NonePrice()
    other_price = MockPrice(100)
    
    assert not none_price.gt(other_price)
