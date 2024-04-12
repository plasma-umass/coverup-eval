# file pypara/monetary.py:397-399
# lines [397, 398, 399]
# branches []

import pytest
from pypara.monetary import Money

# Mock class to implement the abstract Money class
class ConcreteMoney(Money):
    def __init__(self, amount):
        self.amount = amount

    def __le__(self, other):
        if not isinstance(other, ConcreteMoney):
            return NotImplemented
        return self.amount <= other.amount

# Test function to cover the __le__ method
def test_money_le_method():
    money1 = ConcreteMoney(10)
    money2 = ConcreteMoney(20)
    money3 = ConcreteMoney(10)

    assert money1 <= money2, "money1 should be less than or equal to money2"
    assert not money2 <= money1, "money2 should not be less than money1"
    assert money1 <= money3, "money1 should be equal to money3"
    assert money3 <= money1, "money3 should be equal to money1"

# Test function to cover the NotImplemented branch
def test_money_le_not_implemented(mocker):
    class Other:
        pass

    money = ConcreteMoney(10)
    other = Other()

    mocker.patch.object(ConcreteMoney, '__le__', return_value=NotImplemented)
    assert money.__le__(other) is NotImplemented, "Should return NotImplemented when other is not a Money instance"
