# file: pypara/monetary.py:873-880
# asked: {"lines": [873, 874, 880], "branches": []}
# gained: {"lines": [873, 874, 880], "branches": []}

import pytest
from pypara.monetary import Price
from pypara.commons.numbers import Numeric

class ConcretePrice(Price):
    def __init__(self, quantity):
        self.quantity = quantity

    def scalar_subtract(self, other: Numeric) -> 'Price':
        if not isinstance(other, (int, float)):
            raise TypeError("The value must be a numeric type.")
        return ConcretePrice(self.quantity - other)

def test_scalar_subtract():
    price = ConcretePrice(100)
    result = price.scalar_subtract(10)
    assert result.quantity == 90

    with pytest.raises(TypeError):
        price.scalar_subtract("10")

    with pytest.raises(NotImplementedError):
        abstract_price = Price()
        abstract_price.scalar_subtract(10)
