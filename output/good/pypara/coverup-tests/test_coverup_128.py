# file pypara/monetary.py:1085-1087
# lines [1085, 1086, 1087]
# branches []

import pytest
from pypara.monetary import Price

# Mock class to implement the abstract Price class
class ConcretePrice(Price):
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        if not isinstance(other, ConcretePrice):
            return NotImplemented
        return self.value < other.value

# Test function to cover the __lt__ method
def test_price_less_than():
    price1 = ConcretePrice(10)
    price2 = ConcretePrice(20)

    assert price1 < price2, "price1 should be less than price2"
    assert not (price2 < price1), "price2 should not be less than price1"

# Test function to check comparison with non-Price object
def test_price_comparison_with_non_price():
    price1 = ConcretePrice(10)
    price3 = "not_a_price"

    with pytest.raises(TypeError):
        _ = price1 < price3
