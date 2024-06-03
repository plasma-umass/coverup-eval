# file pypara/monetary.py:1030-1032
# lines [1030, 1031, 1032]
# branches []

import pytest
from pypara.monetary import Price

def test_price_abs_method():
    class ConcretePrice(Price):
        def __abs__(self):
            return self

    price_instance = ConcretePrice()
    result = abs(price_instance)
    
    assert result is price_instance
