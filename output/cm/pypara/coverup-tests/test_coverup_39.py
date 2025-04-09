# file pypara/monetary.py:133-138
# lines [133, 134, 138]
# branches []

import pytest
from pypara.monetary import Money

class ConcreteMoney(Money):
    def __init__(self, amount):
        self.amount = amount

    def negative(self):
        return ConcreteMoney(-self.amount)

def test_money_negative():
    original_amount = 100
    money = ConcreteMoney(original_amount)
    negated_money = money.negative()
    
    assert isinstance(negated_money, Money), "The result should be an instance of Money"
    assert negated_money.amount == -original_amount, "The negated amount should be the negative of the original amount"
