# file pypara/monetary.py:882-889
# lines [889]
# branches []

import pytest
from pypara.monetary import Price

class ConcretePrice(Price):
    def multiply(self, other):
        return super().multiply(other)

def test_price_multiply_not_implemented():
    price = ConcretePrice()
    
    with pytest.raises(NotImplementedError):
        price.multiply(1)
