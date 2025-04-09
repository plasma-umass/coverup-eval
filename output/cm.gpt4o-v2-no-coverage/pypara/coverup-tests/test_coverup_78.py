# file: pypara/monetary.py:1077-1079
# asked: {"lines": [1077, 1078, 1079], "branches": []}
# gained: {"lines": [1077, 1078], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import Price
from pypara.commons.numbers import Numeric

class ConcretePrice(Price):
    def __init__(self, value):
        self.value = value

    def __truediv__(self, other: Numeric) -> "ConcretePrice":
        if not isinstance(other, (int, float, Decimal)):
            raise TypeError("Unsupported type for division")
        return ConcretePrice(self.value / other)

def test_price_truediv_int():
    price = ConcretePrice(100)
    result = price / 2
    assert isinstance(result, ConcretePrice)
    assert result.value == 50

def test_price_truediv_float():
    price = ConcretePrice(100)
    result = price / 2.5
    assert isinstance(result, ConcretePrice)
    assert result.value == 40

def test_price_truediv_decimal():
    price = ConcretePrice(Decimal('100'))
    result = price / Decimal('2.5')
    assert isinstance(result, ConcretePrice)
    assert result.value == Decimal('40')

def test_price_truediv_invalid_type():
    price = ConcretePrice(100)
    with pytest.raises(TypeError):
        price / "invalid"

