# file pypara/monetary.py:851-858
# lines [858]
# branches []

import pytest
from pypara.monetary import Price
from decimal import Decimal

class ConcretePrice(Price):
    def scalar_add(self, other):
        return super().scalar_add(other)

def test_scalar_add_not_implemented():
    price = ConcretePrice()
    with pytest.raises(NotImplementedError):
        price.scalar_add(Decimal('10.00'))
