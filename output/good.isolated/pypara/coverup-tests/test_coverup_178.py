# file pypara/monetary.py:1366-1367
# lines [1366, 1367]
# branches []

import pytest
from pypara.monetary import NonePrice, Price

@pytest.fixture
def none_price():
    return NonePrice()

def test_none_price_divide(none_price):
    result = none_price.divide(10)
    assert isinstance(result, Price)
    assert isinstance(result, NonePrice)
