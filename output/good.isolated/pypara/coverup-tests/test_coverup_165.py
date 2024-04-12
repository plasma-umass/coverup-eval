# file pypara/monetary.py:1345-1346
# lines [1345, 1346]
# branches []

import pytest
from pypara.monetary import NonePrice

def test_none_price_positive():
    none_price = NonePrice()
    result = none_price.positive()
    assert isinstance(result, NonePrice), "The result should be an instance of NonePrice"
