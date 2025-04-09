# file: pypara/monetary.py:1061-1063
# asked: {"lines": [1061, 1062, 1063], "branches": []}
# gained: {"lines": [1061, 1062], "branches": []}

import pytest
from abc import ABC, abstractmethod
from pypara.monetary import Price

class ConcretePrice(Price):
    def __pos__(self):
        return self

def test_pos_method():
    price = ConcretePrice()
    result = +price
    assert result is price
