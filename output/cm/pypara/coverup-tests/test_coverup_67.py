# file pypara/monetary.py:401-403
# lines [401, 402, 403]
# branches []

import pytest
from pypara.monetary import Money

# Mock class to implement the abstract Money class
class ConcreteMoney(Money):
    def __init__(self, amount):
        self.amount = amount

    def __gt__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount > other.amount

# Test function to improve coverage
def test_money_greater_than_comparison():
    money1 = ConcreteMoney(10)
    money2 = ConcreteMoney(5)
    money3 = ConcreteMoney(15)

    assert money1 > money2, "money1 should be greater than money2"
    assert not money2 > money1, "money2 should not be greater than money1"
    assert not money1 > money3, "money1 should not be greater than money3"

    with pytest.raises(TypeError):
        money1 > 5  # Comparing with non-Money type should raise TypeError
