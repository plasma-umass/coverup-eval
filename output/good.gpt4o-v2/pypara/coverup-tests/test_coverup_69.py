# file: pypara/monetary.py:882-889
# asked: {"lines": [882, 883, 889], "branches": []}
# gained: {"lines": [882, 883, 889], "branches": []}

import pytest
from pypara.monetary import Price
from pypara.commons.numbers import Numeric

class ConcretePrice(Price):
    def multiply(self, other: Numeric) -> 'Price':
        return self

def test_multiply_not_implemented():
    price = Price()
    with pytest.raises(NotImplementedError):
        price.multiply(10)

def test_concrete_price_multiply():
    price = ConcretePrice()
    result = price.multiply(10)
    assert result is price
