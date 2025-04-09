# file pypara/monetary.py:334-336
# lines [334, 335, 336]
# branches []

import pytest
from pypara.monetary import Money

class ConcreteMoney(Money):
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        if not isinstance(other, ConcreteMoney):
            return False
        return self.amount == other.amount

@pytest.fixture
def money():
    return ConcreteMoney(10)

def test_money_eq(money):
    same_money = ConcreteMoney(10)
    different_money = ConcreteMoney(20)
    non_money = "not a money instance"

    assert money == same_money, "Money instances with the same amount should be equal"
    assert not (money == different_money), "Money instances with different amounts should not be equal"
    assert not (money == non_money), "Money should not be equal to a non-money instance"
