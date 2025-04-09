# file pypara/monetary.py:338-340
# lines [338, 339, 340]
# branches []

import pytest
from pypara.monetary import Money

# Mock class to implement the abstract Money class
class ConcreteMoney(Money):
    def __init__(self, amount):
        self.amount = amount

    def __abs__(self):
        return ConcreteMoney(abs(self.amount))

# Test function to cover the __abs__ method
def test_money_abs():
    mock_money = ConcreteMoney(-10)
    positive_money = abs(mock_money)
    assert isinstance(positive_money, Money)
    assert positive_money.amount == 10

    mock_money = ConcreteMoney(10)
    positive_money = abs(mock_money)
    assert isinstance(positive_money, Money)
    assert positive_money.amount == 10
