# file pypara/monetary.py:900-907
# lines [907]
# branches []

import pytest
from pypara.monetary import Price

class ConcretePrice(Price):
    def divide(self, other):
        return super().divide(other)

def test_price_divide_not_implemented():
    concrete_price = ConcretePrice()
    with pytest.raises(NotImplementedError):
        concrete_price.divide(10)
