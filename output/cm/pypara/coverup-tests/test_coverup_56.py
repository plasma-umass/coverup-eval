# file pypara/monetary.py:295-300
# lines [295, 296, 300]
# branches []

import pytest
from pypara.monetary import Money
from datetime import date

class ConcreteMoney(Money):
    def __init__(self, amount, currency, value_date=None):
        self.amount = amount
        self.currency = currency
        self.value_date = value_date

    def with_dov(self, dov: date) -> "ConcreteMoney":
        if self.amount is not None and self.currency is not None:
            return ConcreteMoney(self.amount, self.currency, dov)
        return self

def test_with_dov_defined_money():
    # Setup
    initial_money = ConcreteMoney(100, 'USD')
    
    # Exercise
    new_money = initial_money.with_dov(date(2023, 1, 1))
    
    # Verify
    assert new_money.amount == initial_money.amount
    assert new_money.currency == initial_money.currency
    assert new_money.value_date == date(2023, 1, 1)
    
    # Cleanup - nothing to do since no external resources were modified
