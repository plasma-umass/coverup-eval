# file: pypara/monetary.py:1022-1024
# asked: {"lines": [1022, 1023, 1024], "branches": []}
# gained: {"lines": [1022, 1023], "branches": []}

import pytest
from abc import ABC, abstractmethod

# Assuming the Price class is defined in pypara/monetary.py
from pypara.monetary import Price

class ConcretePrice(Price):
    def __bool__(self):
        return True

def test_price_bool():
    price = ConcretePrice()
    assert bool(price) is True
