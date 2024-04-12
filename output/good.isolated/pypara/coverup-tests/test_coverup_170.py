# file pypara/monetary.py:1351-1352
# lines [1351, 1352]
# branches []

import pytest
from pypara.monetary import NonePrice, Price

@pytest.fixture
def none_price():
    return NonePrice()

def test_scalar_add(none_price):
    result = none_price.scalar_add(10)
    assert isinstance(result, Price)
    assert isinstance(result, NonePrice)
