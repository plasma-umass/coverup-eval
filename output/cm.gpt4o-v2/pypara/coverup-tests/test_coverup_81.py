# file: pypara/monetary.py:1077-1079
# asked: {"lines": [1077, 1078, 1079], "branches": []}
# gained: {"lines": [1077, 1078], "branches": []}

import pytest
from pypara.monetary import Price
from pypara.commons.numbers import Numeric
from decimal import Decimal

class ConcretePrice(Price):
    def __truediv__(self, other: Numeric) -> "ConcretePrice":
        if not isinstance(other, (int, float, Decimal)):
            raise TypeError("Unsupported type for division")
        # Dummy implementation for testing purposes
        return self

def test_price_truediv():
    price = ConcretePrice()
    
    # Test division with an integer
    result = price.__truediv__(10)
    assert isinstance(result, ConcretePrice)
    
    # Test division with a float
    result = price.__truediv__(10.5)
    assert isinstance(result, ConcretePrice)
    
    # Test division with a Decimal
    result = price.__truediv__(Decimal('10.5'))
    assert isinstance(result, ConcretePrice)
    
    # Test division with an unsupported type
    with pytest.raises(TypeError):
        price.__truediv__("10")

