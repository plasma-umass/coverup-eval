# file: pypara/monetary.py:1026-1028
# asked: {"lines": [1026, 1027, 1028], "branches": []}
# gained: {"lines": [1026, 1027], "branches": []}

import pytest
from abc import ABC, abstractmethod
from typing import Any

# Assuming the Price class is defined in pypara/monetary.py
from pypara.monetary import Price

class ConcretePrice(Price):
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, ConcretePrice):
            return self.amount == other.amount
        return False

def test_price_equality():
    price1 = ConcretePrice(100)
    price2 = ConcretePrice(100)
    price3 = ConcretePrice(200)

    assert price1 == price2
    assert price1 != price3

def test_price_equality_with_non_price():
    price = ConcretePrice(100)
    non_price = "100"

    assert price != non_price
