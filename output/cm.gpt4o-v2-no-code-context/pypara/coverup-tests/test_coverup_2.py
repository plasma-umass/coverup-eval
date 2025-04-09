# file: pypara/accounting/journaling.py:26-50
# asked: {"lines": [26, 27, 32, 35, 38, 40, 41, 49, 50], "branches": []}
# gained: {"lines": [26, 27, 32, 35, 38, 40, 41, 49, 50], "branches": []}

import pytest
from enum import Enum
from pypara.accounting.journaling import Direction

class MockQuantity:
    def __init__(self, value):
        self.value = value

    def is_zero(self):
        return self.value == 0

    def __gt__(self, other):
        return self.value > other

def test_direction_inc():
    quantity = MockQuantity(10)
    direction = Direction.of(quantity)
    assert direction == Direction.INC

def test_direction_dec():
    quantity = MockQuantity(-10)
    direction = Direction.of(quantity)
    assert direction == Direction.DEC

def test_direction_zero():
    quantity = MockQuantity(0)
    with pytest.raises(AssertionError, match="Encountered a `0` quantity. This implies a programming error."):
        Direction.of(quantity)
