# file pypara/monetary.py:1357-1358
# lines [1357, 1358]
# branches []

import pytest
from pypara.monetary import NonePrice, Price

@pytest.fixture
def none_price():
    return NonePrice()

def test_scalar_subtract(none_price):
    result = none_price.scalar_subtract(10)
    assert isinstance(result, Price)
    assert isinstance(result, NonePrice)
