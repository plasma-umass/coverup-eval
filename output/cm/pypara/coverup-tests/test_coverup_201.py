# file pypara/monetary.py:190-197
# lines [197]
# branches []

import pytest
from pypara.monetary import Money
from decimal import Decimal

class ConcreteMoney(Money):
    def scalar_subtract(self, other):
        return super().scalar_subtract(other)

def test_scalar_subtract_not_implemented(mocker):
    money = ConcreteMoney()
    with pytest.raises(NotImplementedError):
        money.scalar_subtract(Decimal('10.00'))
