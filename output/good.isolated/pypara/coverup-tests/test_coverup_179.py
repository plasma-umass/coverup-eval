# file pypara/monetary.py:1369-1370
# lines [1369, 1370]
# branches []

import pytest
from pypara.monetary import NonePrice, Price

@pytest.fixture
def none_price():
    return NonePrice()

def test_none_price_floor_divide(none_price):
    result = none_price.floor_divide(10)
    assert isinstance(result, NonePrice), "The result should be an instance of NonePrice"
