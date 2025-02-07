# file: pypara/accounting/journaling.py:26-50
# asked: {"lines": [26, 27, 32, 35, 38, 40, 41, 49, 50], "branches": []}
# gained: {"lines": [26, 27, 32, 35, 38, 40, 41, 49, 50], "branches": []}

import pytest
from decimal import Decimal
from pypara.accounting.journaling import Direction
from pypara.commons.numbers import Quantity

def test_direction_of_positive_quantity():
    quantity = Quantity(Decimal(5))
    direction = Direction.of(quantity)
    assert direction == Direction.INC

def test_direction_of_negative_quantity():
    quantity = Quantity(Decimal(-5))
    direction = Direction.of(quantity)
    assert direction == Direction.DEC

def test_direction_of_zero_quantity():
    quantity = Quantity(Decimal(0))
    with pytest.raises(AssertionError, match="Encountered a `0` quantity. This implies a programming error."):
        Direction.of(quantity)
