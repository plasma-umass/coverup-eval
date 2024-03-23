# file pypara/monetary.py:100-110
# lines [100, 101, 110]
# branches []

import pytest
from pypara.monetary import Money

class ConcreteMoney(Money):
    def __init__(self, amount):
        self.amount = amount

    def as_boolean(self):
        return self.amount != 0

@pytest.fixture
def money_fixture():
    return ConcreteMoney(0), ConcreteMoney(10)

def test_as_boolean(money_fixture):
    zero_money, nonzero_money = money_fixture
    assert not zero_money.as_boolean()
    assert nonzero_money.as_boolean()
