# file pypara/monetary.py:838-849
# lines [849]
# branches []

import pytest
from pypara.monetary import Price, IncompatibleCurrencyError

class ConcretePrice(Price):
    def add(self, other: "Price") -> "Price":
        return super().add(other)

def test_price_add_not_implemented():
    price = ConcretePrice()
    with pytest.raises(NotImplementedError):
        price.add(ConcretePrice())
