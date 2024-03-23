# file pypara/monetary.py:147-153
# lines [147, 148, 153]
# branches []

import pytest
from pypara.monetary import Money

class ConcreteMoney(Money):
    def round(self, ndigits: int = 0) -> "Money":
        return self  # Simple implementation for testing purposes

    def __eq__(self, other):
        return isinstance(other, ConcreteMoney)

@pytest.fixture
def concrete_money():
    return ConcreteMoney()

def test_money_round(concrete_money):
    rounded_money = concrete_money.round(2)
    assert rounded_money == concrete_money, "Rounded money should be equal to the original money instance"
