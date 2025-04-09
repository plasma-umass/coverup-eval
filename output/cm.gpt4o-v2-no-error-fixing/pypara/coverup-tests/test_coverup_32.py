# file: pypara/monetary.py:900-907
# asked: {"lines": [900, 901, 907], "branches": []}
# gained: {"lines": [900, 901, 907], "branches": []}

import pytest
from pypara.monetary import Price
from pypara.commons.numbers import Numeric

class ConcretePrice(Price):
    def __init__(self, value):
        self.value = value

    def divide(self, other: Numeric) -> 'Price':
        if other == 0:
            raise ZeroDivisionError("Division by zero is undefined")
        return ConcretePrice(self.value / other)

def test_divide_not_implemented():
    price = Price()
    with pytest.raises(NotImplementedError):
        price.divide(10)

def test_concrete_price_divide():
    price = ConcretePrice(100)
    result = price.divide(2)
    assert isinstance(result, ConcretePrice)
    assert result.value == 50

    with pytest.raises(ZeroDivisionError):
        price.divide(0)
