# file pypara/monetary.py:1034-1036
# lines [1036]
# branches []

import pytest
from pypara.monetary import Price

class ConcretePrice(Price):
    pass

def test_concrete_price_float():
    price = ConcretePrice()
    with pytest.raises(TypeError):
        float(price)
