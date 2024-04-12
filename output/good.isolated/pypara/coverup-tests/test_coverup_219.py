# file pypara/monetary.py:783-793
# lines [793]
# branches []

import pytest
from pypara.monetary import Price

class ConcretePrice(Price):
    pass

def test_price_as_boolean_not_implemented():
    price = ConcretePrice()
    with pytest.raises(NotImplementedError):
        price.as_boolean()
