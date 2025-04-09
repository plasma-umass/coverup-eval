# file: pypara/monetary.py:1384-1385
# asked: {"lines": [1384, 1385], "branches": []}
# gained: {"lines": [1384, 1385], "branches": []}

import pytest
from pypara.monetary import Price, NonePrice, Currency

def test_none_price_with_ccy():
    none_price = NonePrice()
    ccy = Currency(code="USD", name="US Dollar", decimals=2, type="fiat", quantizer=None, hashcache=None)
    result = none_price.with_ccy(ccy)
    
    assert result is none_price
