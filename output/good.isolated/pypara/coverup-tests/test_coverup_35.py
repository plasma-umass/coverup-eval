# file pypara/monetary.py:126-131
# lines [126, 127, 131]
# branches []

import pytest
from pypara.monetary import Money

class ConcreteMoney(Money):
    def __init__(self, amount):
        self.amount = amount

    def abs(self):
        return ConcreteMoney(abs(self.amount))

def test_money_abs():
    positive_money = ConcreteMoney(100)
    negative_money = ConcreteMoney(-100)

    assert positive_money.abs().amount == 100
    assert negative_money.abs().amount == 100
