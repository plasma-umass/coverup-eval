# file: pypara/monetary.py:1081-1083
# asked: {"lines": [1081, 1082, 1083], "branches": []}
# gained: {"lines": [1081, 1082], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import Price
from pypara.commons.numbers import Numeric

class ConcretePrice(Price):
    def __floordiv__(self, other: Numeric) -> "Price":
        return self

def test_floordiv():
    price = ConcretePrice()
    result = price.__floordiv__(10)
    assert isinstance(result, ConcretePrice)
