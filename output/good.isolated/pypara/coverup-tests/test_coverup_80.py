# file pypara/monetary.py:809-814
# lines [809, 810, 814]
# branches []

import pytest
from pypara.monetary import Price

class ConcretePrice(Price):
    def __init__(self, value):
        self.value = value

    def abs(self):
        return ConcretePrice(abs(self.value))

def test_price_abs():
    price = ConcretePrice(-10)
    abs_price = price.abs()
    assert isinstance(abs_price, Price)
    assert abs_price.value == 10

    positive_price = ConcretePrice(20)
    abs_positive_price = positive_price.abs()
    assert isinstance(abs_positive_price, Price)
    assert abs_positive_price.value == 20
