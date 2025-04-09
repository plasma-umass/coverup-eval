# file: pypara/monetary.py:1378-1379
# asked: {"lines": [1378, 1379], "branches": []}
# gained: {"lines": [1378, 1379], "branches": []}

import pytest
from pypara.monetary import Price, NonePrice

def test_noneprice_gt():
    none_price = NonePrice()
    other_price = Price()  # Assuming Price can be initialized without arguments

    assert not none_price.gt(other_price)
    assert not none_price.gt(NonePrice())
