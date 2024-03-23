# file pypara/monetary.py:377-379
# lines [377, 378, 379]
# branches []

import pytest
from pypara.monetary import Money

class ConcreteMoney(Money):
    def __init__(self, amount):
        self.amount = amount

    def __sub__(self, other):
        if not isinstance(other, Money):
            raise TypeError("Subtraction can only be performed with another Money instance")
        return ConcreteMoney(self.amount - other.amount)

@pytest.fixture
def money_fixture():
    # Setup
    money1 = ConcreteMoney(100)
    money2 = ConcreteMoney(50)
    yield money1, money2
    # Teardown
    del money1
    del money2

def test_money_subtraction(money_fixture):
    money1, money2 = money_fixture
    result = money1 - money2
    assert isinstance(result, Money), "The result of subtraction should be an instance of Money"
    assert result.amount == 50, "Subtraction result should be the difference of the two amounts"

def test_money_subtraction_with_non_money():
    money = ConcreteMoney(100)
    with pytest.raises(TypeError):
        money - 10  # Subtracting a non-Money instance should raise TypeError
