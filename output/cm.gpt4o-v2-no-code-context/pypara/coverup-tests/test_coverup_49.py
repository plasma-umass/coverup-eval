# file: pypara/monetary.py:909-917
# asked: {"lines": [909, 910, 917], "branches": []}
# gained: {"lines": [909, 910, 917], "branches": []}

import pytest
from pypara.monetary import Price

class ConcretePrice(Price):
    def floor_divide(self, other):
        super().floor_divide(other)

def test_price_floor_divide_not_implemented():
    price = ConcretePrice()
    with pytest.raises(NotImplementedError):
        price.floor_divide(10)
