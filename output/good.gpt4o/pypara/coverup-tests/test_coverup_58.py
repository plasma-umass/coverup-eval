# file pypara/monetary.py:1073-1075
# lines [1073, 1074, 1075]
# branches []

import pytest
from pypara.monetary import Price

def test_price_mul_abstract_method():
    class TestPrice(Price):
        def __mul__(self, other):
            return self

    price_instance = TestPrice()
    result = price_instance * 10
    assert isinstance(result, TestPrice)
