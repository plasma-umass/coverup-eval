# file pypara/monetary.py:1061-1063
# lines [1061, 1062, 1063]
# branches []

import pytest
from abc import ABC, abstractmethod

# Assuming the Price class is defined in pypara.monetary
from pypara.monetary import Price

class ConcretePrice(Price):
    def __pos__(self):
        return self

def test_price_pos_method():
    price = ConcretePrice()
    result = +price
    assert result is price

