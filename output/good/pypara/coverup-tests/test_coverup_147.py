# file pypara/monetary.py:665-666
# lines [665, 666]
# branches []

import pytest
from pypara.monetary import NoneMoney, Money
from decimal import Decimal

@pytest.fixture
def none_money():
    return NoneMoney()

def test_none_money_multiply(none_money):
    # Test multiplication with an integer
    result = none_money.multiply(2)
    assert isinstance(result, Money)
    assert result is none_money  # Ensure it returns the same instance

    # Test multiplication with a float
    result = none_money.multiply(2.5)
    assert isinstance(result, Money)
    assert result is none_money  # Ensure it returns the same instance

    # Test multiplication with a Decimal
    result = none_money.multiply(Decimal('3.5'))
    assert isinstance(result, Money)
    assert result is none_money  # Ensure it returns the same instance
