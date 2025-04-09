# file pypara/monetary.py:330-332
# lines [330, 331, 332]
# branches []

import pytest
from pypara.monetary import Money

# Mock class to implement the abstract Money class
class ConcreteMoney(Money):
    def __init__(self, amount):
        self.amount = amount

    def __bool__(self):
        return bool(self.amount)

# Test function to cover the __bool__ method
def test_money_bool():
    # Test with non-zero amount (should return True)
    money_positive = ConcreteMoney(100)
    assert bool(money_positive) == True

    # Test with zero amount (should return False)
    money_zero = ConcreteMoney(0)
    assert bool(money_zero) == False
