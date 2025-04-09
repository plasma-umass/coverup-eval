# file pypara/monetary.py:909-917
# lines [909, 910, 917]
# branches []

import pytest
from pypara.monetary import Price
from decimal import Decimal

class ConcretePrice(Price):
    def __init__(self, amount):
        self.amount = Decimal(amount)

    def floor_divide(self, other):
        if other == 0:
            return None  # Represents an undefined price object
        return ConcretePrice(self.amount // Decimal(other))

def test_floor_divide():
    price = ConcretePrice(100)
    result = price.floor_divide(3)
    assert isinstance(result, ConcretePrice)
    assert result.amount == Decimal('33')

    result = price.floor_divide(0)
    assert result is None

def test_floor_divide_not_implemented_error():
    with pytest.raises(NotImplementedError):
        Price().floor_divide(1)
