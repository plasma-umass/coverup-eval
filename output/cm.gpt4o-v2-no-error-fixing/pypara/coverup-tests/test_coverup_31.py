# file: pypara/monetary.py:851-858
# asked: {"lines": [851, 852, 858], "branches": []}
# gained: {"lines": [851, 852, 858], "branches": []}

import pytest
from pypara.monetary import Price
from pypara.commons.numbers import Numeric

class ConcretePrice(Price):
    def scalar_add(self, other: Numeric) -> "Price":
        return self

def test_scalar_add_not_implemented():
    price = Price()
    with pytest.raises(NotImplementedError):
        price.scalar_add(10)

def test_concrete_price_scalar_add():
    price = ConcretePrice()
    result = price.scalar_add(10)
    assert result is price
