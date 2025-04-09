# file pypara/monetary.py:809-814
# lines [814]
# branches []

import pytest
from pypara.monetary import Price

class ConcretePrice(Price):
    def abs(self):
        return super().abs()

def test_price_abs_not_implemented():
    price = ConcretePrice()
    with pytest.raises(NotImplementedError):
        price.abs()
