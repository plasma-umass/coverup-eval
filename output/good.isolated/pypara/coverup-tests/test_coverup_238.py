# file pypara/monetary.py:100-110
# lines [110]
# branches []

import pytest
from pypara.monetary import Money

class ConcreteMoney(Money):
    def __init__(self, amount):
        self.amount = amount

    def as_boolean(self):
        if self.amount is None or self.amount == 0:
            return False
        else:
            return True

@pytest.fixture
def concrete_money():
    return ConcreteMoney(0)

def test_as_boolean_with_zero_amount(concrete_money):
    assert concrete_money.as_boolean() is False

def test_as_boolean_with_non_zero_amount():
    money = ConcreteMoney(100)
    assert money.as_boolean() is True

def test_as_boolean_with_undefined_amount():
    money = ConcreteMoney(None)
    assert money.as_boolean() is False

def test_as_boolean_raises_not_implemented_error():
    with pytest.raises(NotImplementedError):
        Money().as_boolean()
