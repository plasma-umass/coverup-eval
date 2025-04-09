# file pypara/monetary.py:1065-1067
# lines [1065, 1066, 1067]
# branches []

import pytest
from pypara.monetary import Price

class ConcretePrice(Price):
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        if not isinstance(other, ConcretePrice):
            return NotImplemented
        return ConcretePrice(self.amount + other.amount)

@pytest.fixture
def price():
    return ConcretePrice(10)

@pytest.fixture
def other_price():
    return ConcretePrice(5)

def test_price_addition(price, other_price):
    result = price + other_price
    assert isinstance(result, ConcretePrice)
    assert result.amount == 15

def test_price_addition_with_non_price_object(price):
    with pytest.raises(TypeError):
        result = price + 3  # Adding a non-Price object
