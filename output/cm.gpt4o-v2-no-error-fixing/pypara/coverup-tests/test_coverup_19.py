# file: pypara/monetary.py:295-300
# asked: {"lines": [295, 296, 300], "branches": []}
# gained: {"lines": [295, 296], "branches": []}

import pytest
from abc import ABC
from pypara.monetary import Money
from pypara.commons.zeitgeist import Date

class ConcreteMoney(Money, ABC):
    def with_dov(self, dov: Date) -> "Money":
        return self

def test_with_dov():
    money = ConcreteMoney()
    dov = Date.today()
    result = money.with_dov(dov)
    assert result is money
