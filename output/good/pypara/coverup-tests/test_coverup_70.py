# file pypara/monetary.py:816-821
# lines [816, 817, 821]
# branches []

import pytest
from pypara.monetary import Price

class ConcretePrice(Price):
    def __init__(self, amount):
        self.amount = amount

    def negative(self):
        return ConcretePrice(-self.amount)

def test_price_negative():
    price = ConcretePrice(100)
    negative_price = price.negative()

    assert isinstance(negative_price, Price)
    assert negative_price.amount == -100
