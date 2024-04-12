# file pypara/monetary.py:891-898
# lines [891, 892, 898]
# branches []

import pytest
from pypara.monetary import Price
from decimal import Decimal
from typing import Union

Numeric = Union[int, Decimal]

class ConcretePrice(Price):
    def times(self, other: Numeric) -> "ConcretePrice":
        return ConcretePrice()

def test_price_times_not_implemented():
    class TestPrice(Price):
        pass

    with pytest.raises(NotImplementedError):
        TestPrice().times(2)

def test_concrete_price_times():
    price = ConcretePrice()
    result = price.times(2)
    assert isinstance(result, ConcretePrice)

# Assuming the test file is named test_monetary.py
# To run the tests, use the following command:
# pytest test_monetary.py
