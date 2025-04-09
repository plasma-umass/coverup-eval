# file: pypara/monetary.py:168-175
# asked: {"lines": [175], "branches": []}
# gained: {"lines": [175], "branches": []}

import pytest
from pypara.monetary import Money

class ConcreteMoney(Money):
    def scalar_add(self, other):
        super().scalar_add(other)

def test_scalar_add_not_implemented():
    money = ConcreteMoney()
    with pytest.raises(NotImplementedError):
        money.scalar_add(10)
