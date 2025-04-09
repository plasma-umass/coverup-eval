# file pypara/monetary.py:771-781
# lines [781]
# branches []

import pytest
from pypara.monetary import Price
from typing import Any

class ConcretePrice(Price):
    def is_equal(self, other: Any) -> bool:
        return super().is_equal(other)

def test_price_is_equal_not_implemented():
    price = ConcretePrice()
    with pytest.raises(NotImplementedError):
        price.is_equal(None)
