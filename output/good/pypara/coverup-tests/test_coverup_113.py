# file pypara/monetary.py:1093-1095
# lines [1093, 1094, 1095]
# branches []

import pytest
from pypara.monetary import Price

# Mock class to implement the abstract Price class
class ConcretePrice(Price):
    def __init__(self, value):
        self.value = value

    def __gt__(self, other):
        if not isinstance(other, ConcretePrice):
            return NotImplemented
        return self.value > other.value

# Test function to cover the __gt__ method
def test_price_greater_than():
    price1 = ConcretePrice(10)
    price2 = ConcretePrice(5)
    price3 = ConcretePrice(10)

    assert price1 > price2, "price1 should be greater than price2"
    assert not price2 > price1, "price2 should not be greater than price1"
    assert not price1 > price3, "price1 should not be greater than price3 (equal values)"
    with pytest.raises(TypeError):
        price1 > "non-price"
