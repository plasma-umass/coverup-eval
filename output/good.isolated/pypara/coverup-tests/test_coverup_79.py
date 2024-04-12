# file pypara/monetary.py:405-407
# lines [405, 406, 407]
# branches []

import pytest
from pypara.monetary import Money

class ConcreteMoney(Money):
    def __init__(self, amount):
        self.amount = amount

    def __ge__(self, other):
        if not isinstance(other, ConcreteMoney):
            return NotImplemented
        return self.amount >= other.amount

@pytest.fixture
def money_cleanup():
    # Setup code if necessary
    yield
    # Cleanup code if necessary

def test_money_ge(money_cleanup):
    money1 = ConcreteMoney(10)
    money2 = ConcreteMoney(5)
    money3 = ConcreteMoney(10)
    
    assert money1 >= money2, "money1 should be greater than or equal to money2"
    assert not (money2 >= money1), "money2 should not be greater than money1"
    assert money1 >= money3, "money1 should be equal to money3"
    assert money3 >= money1, "money3 should be equal to money1"
    assert money1 >= money1, "money1 should be equal to itself"
    
    with pytest.raises(TypeError):
        money1 >= 5  # Comparing with a non-Money type should raise TypeError
