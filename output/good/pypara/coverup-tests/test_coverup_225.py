# file pypara/monetary.py:873-880
# lines [880]
# branches []

import pytest
from pypara.monetary import Price
from decimal import Decimal

class ConcretePrice(Price):
    def scalar_subtract(self, other):
        return super().scalar_subtract(other)

def test_scalar_subtract_not_implemented(mocker):
    price = ConcretePrice()
    with pytest.raises(NotImplementedError):
        price.scalar_subtract(Decimal('10.00'))
