# file: pypara/monetary.py:1324-1325
# asked: {"lines": [1324, 1325], "branches": []}
# gained: {"lines": [1324, 1325], "branches": []}

import pytest
from pypara.monetary import NonePrice

def test_none_price_as_boolean():
    none_price = NonePrice()
    assert not none_price.as_boolean()
    assert not bool(none_price)
