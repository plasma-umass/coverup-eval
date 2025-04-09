# file: pypara/monetary.py:900-907
# asked: {"lines": [900, 901, 907], "branches": []}
# gained: {"lines": [900, 901, 907], "branches": []}

import pytest
from pypara.monetary import Price

class ConcretePrice(Price):
    def __init__(self, value):
        self.value = value

    def divide(self, other: float) -> "ConcretePrice":
        if other == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return ConcretePrice(self.value / other)

def test_divide_abstract_method():
    with pytest.raises(NotImplementedError):
        price = Price()
        price.divide(1)

def test_concrete_price_divide():
    price = ConcretePrice(100)
    result = price.divide(2)
    assert result.value == 50

    with pytest.raises(ZeroDivisionError):
        price.divide(0)
