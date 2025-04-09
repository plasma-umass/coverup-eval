# file: pypara/monetary.py:771-781
# asked: {"lines": [781], "branches": []}
# gained: {"lines": [781], "branches": []}

import pytest
from pypara.monetary import Price
from typing import Any

class ConcretePrice(Price):
    def is_equal(self, other: Any) -> bool:
        return False

def test_price_is_equal_not_implemented():
    with pytest.raises(NotImplementedError):
        class AbstractPrice(Price):
            pass
        price = AbstractPrice()
        price.is_equal(None)

def test_concreteprice_is_equal():
    price = ConcretePrice()
    assert not price.is_equal(None)
