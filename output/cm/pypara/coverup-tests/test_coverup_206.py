# file pypara/monetary.py:147-153
# lines [153]
# branches []

import pytest
from pypara.monetary import Money

class ConcreteMoney(Money):
    def round(self, ndigits: int = 0) -> "Money":
        return self  # Just a simple implementation for testing purposes

@pytest.fixture
def concrete_money():
    return ConcreteMoney()

def test_money_round_not_implemented_error(concrete_money):
    with pytest.raises(NotImplementedError):
        Money.round(concrete_money)
