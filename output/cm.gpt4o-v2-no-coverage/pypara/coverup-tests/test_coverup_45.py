# file: pypara/monetary.py:365-367
# asked: {"lines": [365, 366, 367], "branches": []}
# gained: {"lines": [365, 366], "branches": []}

import pytest
from abc import ABC, abstractmethod
from pypara.monetary import Money

class ConcreteMoney(Money):
    def __neg__(self):
        return self

def test_neg_method():
    money = ConcreteMoney()
    result = -money
    assert result is money
