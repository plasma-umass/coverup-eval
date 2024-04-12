# file pypara/monetary.py:1097-1099
# lines [1097, 1098, 1099]
# branches []

import pytest
from pypara.monetary import Price

class ConcretePrice(Price):
    def __init__(self, amount):
        self.amount = amount

    def __ge__(self, other):
        if not isinstance(other, ConcretePrice):
            return NotImplemented
        return self.amount >= other.amount

def test_price_comparison(mocker):
    # Create two price instances
    price1 = ConcretePrice(10)
    price2 = ConcretePrice(5)
    price3 = ConcretePrice(15)

    # Test __ge__ method
    assert price1 >= price2, "price1 should be greater than or equal to price2"
    assert not (price2 >= price1), "price2 should not be greater than or equal to price1"
    assert price1 >= price1, "price1 should be greater than or equal to itself"
    assert price3 >= price1, "price3 should be greater than or equal to price1"

    # Test comparison with a non-Price instance
    with pytest.raises(TypeError):
        price1 >= 10

    # Clean up by mocking the abstract method to prevent side effects
    mocker.patch.object(Price, '__ge__', return_value=NotImplemented)
