# file pypara/monetary.py:1316-1323
# lines [1316, 1318, 1320, 1322]
# branches []

import pytest
from pypara.monetary import NonePrice, Price

def test_none_price():
    none_price = NonePrice()
    
    assert none_price.defined is False
    assert none_price.undefined is True
    assert isinstance(none_price, Price)
