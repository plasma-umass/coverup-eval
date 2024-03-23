# file pypara/monetary.py:365-367
# lines [365, 366, 367]
# branches []

import pytest
from pypara.monetary import Money

class ConcreteMoney(Money):
    def __init__(self, amount):
        self.amount = amount

    def __neg__(self):
        return ConcreteMoney(-self.amount)

def test_money_negation():
    original_money = ConcreteMoney(100)
    negated_money = -original_money

    assert isinstance(negated_money, Money)
    assert negated_money.amount == -original_money.amount

    # Clean up (nothing to clean up in this case as no external resources are used)
