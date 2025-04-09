# file: pypara/monetary.py:1073-1075
# asked: {"lines": [1073, 1074, 1075], "branches": []}
# gained: {"lines": [1073, 1074], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import Price
from pypara.commons.numbers import Numeric

class ConcretePrice(Price):
    def __init__(self, amount: Numeric):
        self.amount = amount

    def __mul__(self, other: Numeric) -> 'ConcretePrice':
        return ConcretePrice(self.amount * other)

def test_price_mul():
    price = ConcretePrice(100)
    result = price * 2
    assert isinstance(result, ConcretePrice)
    assert result.amount == 200

    result = price * 2.5
    assert isinstance(result, ConcretePrice)
    assert result.amount == 250

    result = price * Decimal('1.5')
    assert isinstance(result, ConcretePrice)
    assert result.amount == Decimal('150')
