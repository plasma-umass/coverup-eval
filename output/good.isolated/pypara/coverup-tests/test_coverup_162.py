# file pypara/monetary.py:1342-1343
# lines [1342, 1343]
# branches []

import pytest
from pypara.monetary import NonePrice

def test_none_price_negative():
    none_price = NonePrice()
    result = none_price.negative()
    assert result is none_price, "The negative method on NonePrice should return self"
