# file pypara/monetary.py:1089-1091
# lines [1089, 1090, 1091]
# branches []

import pytest
from pypara.monetary import Price

# Mock class to implement the abstract Price class
class ConcretePrice(Price):
    def __init__(self, value):
        self.value = value

    def __le__(self, other):
        if not isinstance(other, ConcretePrice):
            return NotImplemented
        return self.value <= other.value

# Test function to cover the __le__ method
def test_price_less_than_or_equal():
    price1 = ConcretePrice(10)
    price2 = ConcretePrice(20)
    price3 = ConcretePrice(10)

    assert price1 <= price2, "price1 should be less than or equal to price2"
    assert price1 <= price3, "price1 should be equal to price3"
    assert not price2 <= price1, "price2 should not be less than price1"

    with pytest.raises(TypeError):
        price1 <= 10  # Comparing with a non-Price type should raise TypeError

# Test function to cover the NotImplemented branch
def test_price_less_than_or_equal_not_implemented():
    price1 = ConcretePrice(10)
    other = object()  # Using a plain object to trigger the NotImplemented branch

    # Check that TypeError is raised when other is not a ConcretePrice instance
    with pytest.raises(TypeError):
        price1 <= other
