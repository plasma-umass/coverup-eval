# file pypara/monetary.py:88-98
# lines [88, 89, 98]
# branches []

import pytest
from pypara.monetary import Money

class ConcreteMoney(Money):
    __slots__ = ('amount', 'currency')

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def is_equal(self, other):
        if isinstance(other, Money):
            return all(getattr(self, slot) == getattr(other, slot) for slot in self.__slots__)
        return False

@pytest.fixture
def money_objects():
    money1 = ConcreteMoney(100, 'USD')
    money2 = ConcreteMoney(100, 'USD')
    money3 = ConcreteMoney(200, 'USD')
    money4 = ConcreteMoney(100, 'EUR')
    return money1, money2, money3, money4

def test_money_is_equal(money_objects):
    money1, money2, money3, money4 = money_objects

    # Test equality with the same attributes
    assert money1.is_equal(money2) == True

    # Test inequality with different amount
    assert money1.is_equal(money3) == False

    # Test inequality with different currency
    assert money1.is_equal(money4) == False

    # Test inequality with non-money object
    assert money1.is_equal(100) == False
