# file: pypara/monetary.py:873-880
# asked: {"lines": [880], "branches": []}
# gained: {"lines": [880], "branches": []}

import pytest
from pypara.monetary import Price
from pypara.commons.numbers import Numeric

class ConcretePrice(Price):
    def __init__(self, value: Numeric):
        self.value = value

    def scalar_subtract(self, other: Numeric) -> "ConcretePrice":
        if self.value is None:
            return self
        return ConcretePrice(self.value - other)

def test_scalar_subtract():
    price = ConcretePrice(100)
    result = price.scalar_subtract(50)
    assert result.value == 50

    price = ConcretePrice(None)
    result = price.scalar_subtract(50)
    assert result.value is None

def test_scalar_subtract_not_implemented():
    with pytest.raises(NotImplementedError):
        price = Price()
        price.scalar_subtract(50)
