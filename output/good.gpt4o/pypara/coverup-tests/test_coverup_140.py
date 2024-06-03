# file pypara/accounting/journaling.py:26-50
# lines [49, 50]
# branches []

import pytest
from pypara.accounting.journaling import Direction

class MockQuantity:
    def __init__(self, value):
        self.value = value

    def is_zero(self):
        return self.value == 0

    def __gt__(self, other):
        return self.value > other

def test_direction_of_zero_quantity():
    zero_quantity = MockQuantity(0)
    with pytest.raises(AssertionError, match="Encountered a `0` quantity. This implies a programming error."):
        Direction.of(zero_quantity)

def test_direction_of_positive_quantity():
    positive_quantity = MockQuantity(1)
    direction = Direction.of(positive_quantity)
    assert direction == Direction.INC

def test_direction_of_negative_quantity():
    negative_quantity = MockQuantity(-1)
    direction = Direction.of(negative_quantity)
    assert direction == Direction.DEC
