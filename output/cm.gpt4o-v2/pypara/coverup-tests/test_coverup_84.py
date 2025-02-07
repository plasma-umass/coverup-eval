# file: pypara/monetary.py:1089-1091
# asked: {"lines": [1089, 1090, 1091], "branches": []}
# gained: {"lines": [1089, 1090], "branches": []}

import pytest
from pypara.monetary import Price

class ConcretePrice(Price):
    def __init__(self, amount):
        self.amount = amount

    def __le__(self, other: 'ConcretePrice') -> bool:
        return self.amount <= other.amount

def test_price_le():
    price1 = ConcretePrice(100)
    price2 = ConcretePrice(200)
    price3 = ConcretePrice(100)

    assert price1 <= price2
    assert price1 <= price3
    assert not (price2 <= price1)
