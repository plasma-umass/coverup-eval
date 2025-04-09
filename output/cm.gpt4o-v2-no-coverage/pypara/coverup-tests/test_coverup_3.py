# file: pypara/accounting/journaling.py:26-50
# asked: {"lines": [26, 27, 32, 35, 38, 40, 41, 49, 50], "branches": []}
# gained: {"lines": [26, 27, 32, 35, 38, 40, 41, 49, 50], "branches": []}

import pytest
from decimal import Decimal
from pypara.commons.numbers import Quantity
from pypara.accounting.journaling import Direction

def test_direction_of_inc():
    quantity = Quantity(Decimal('1.0'))
    direction = Direction.of(quantity)
    assert direction == Direction.INC

def test_direction_of_dec():
    quantity = Quantity(Decimal('-1.0'))
    direction = Direction.of(quantity)
    assert direction == Direction.DEC

def test_direction_of_zero():
    quantity = Quantity(Decimal('0.0'))
    with pytest.raises(AssertionError, match="Encountered a `0` quantity. This implies a programming error."):
        Direction.of(quantity)
