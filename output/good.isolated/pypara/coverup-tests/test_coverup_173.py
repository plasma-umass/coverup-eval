# file pypara/monetary.py:1360-1361
# lines [1360, 1361]
# branches []

import pytest
from pypara.monetary import NonePrice, Price

@pytest.fixture
def none_price():
    return NonePrice()

def test_none_price_multiply(none_price):
    result = none_price.multiply(10)
    assert isinstance(result, Price)
    assert isinstance(result, NonePrice)
