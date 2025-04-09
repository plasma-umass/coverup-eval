# file: pypara/monetary.py:851-858
# asked: {"lines": [851, 852, 858], "branches": []}
# gained: {"lines": [851, 852, 858], "branches": []}

import pytest
from pypara.monetary import Price

class ConcretePrice(Price):
    def scalar_add(self, other) -> "Price":
        return self

def test_scalar_add_not_implemented():
    class AbstractPrice(Price):
        pass

    with pytest.raises(NotImplementedError):
        price = AbstractPrice()
        price.scalar_add(10)

def test_scalar_add_implemented():
    price = ConcretePrice()
    result = price.scalar_add(10)
    assert result is price
