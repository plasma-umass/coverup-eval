# file pypara/monetary.py:1022-1024
# lines [1022, 1023, 1024]
# branches []

import pytest
from pypara.monetary import Price

class ConcretePrice(Price):
    def __init__(self, value):
        self.value = value

    def __bool__(self):
        return bool(self.value)

def test_price_bool():
    price_true = ConcretePrice(100)
    price_false = ConcretePrice(0)

    assert bool(price_true) is True
    assert bool(price_false) is False
