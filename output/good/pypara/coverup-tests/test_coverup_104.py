# file pypara/monetary.py:1057-1059
# lines [1057, 1058, 1059]
# branches []

import pytest
from pypara.monetary import Price

class ConcretePrice(Price):
    def __init__(self, amount):
        self.amount = amount

    def __neg__(self):
        return ConcretePrice(-self.amount)

def test_price_negation():
    price = ConcretePrice(100)
    negated_price = -price

    assert isinstance(negated_price, Price)
    assert negated_price.amount == -100
