# file pypara/monetary.py:168-175
# lines [175]
# branches []

import pytest
from pypara.monetary import Money
from decimal import Decimal

class DummyMoney(Money):
    def scalar_add(self, other):
        return super().scalar_add(other)

def test_scalar_add_not_implemented(mocker):
    dummy_money = DummyMoney()
    with pytest.raises(NotImplementedError):
        dummy_money.scalar_add(Decimal('10.00'))
