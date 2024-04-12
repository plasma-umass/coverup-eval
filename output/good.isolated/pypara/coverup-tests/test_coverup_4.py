# file pypara/accounting/journaling.py:26-50
# lines [26, 27, 32, 35, 38, 40, 41, 49, 50]
# branches []

import pytest
from pypara.accounting.journaling import Direction
from decimal import Decimal

@pytest.fixture
def cleanup():
    # Setup code if necessary
    yield
    # Cleanup code if necessary

def test_direction_of_positive_quantity(cleanup):
    positive_quantity = Decimal('10.0')
    direction = Direction.of(positive_quantity)
    assert direction == Direction.INC

def test_direction_of_negative_quantity(cleanup):
    negative_quantity = Decimal('-5.0')
    direction = Direction.of(negative_quantity)
    assert direction == Direction.DEC

def test_direction_of_zero_quantity_raises_assertion_error(cleanup):
    zero_quantity = Decimal('0.0')
    with pytest.raises(AssertionError, match="Encountered a `0` quantity. This implies a programming error."):
        Direction.of(zero_quantity)
