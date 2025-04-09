# file pypara/monetary.py:656-657
# lines [656, 657]
# branches []

import pytest
from pypara.monetary import NoneMoney, Money
from decimal import Decimal

@pytest.fixture
def none_money():
    return NoneMoney()

def test_scalar_add(none_money):
    result = none_money.scalar_add(Decimal('10.00'))
    assert isinstance(result, Money)
    assert result is none_money  # Ensure that the same instance is returned
