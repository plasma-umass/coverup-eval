# file pymonet/either.py:17-20
# lines [17, 18, 19, 20]
# branches []

import pytest
from pymonet.either import Either, Left, Right

def test_either_equality():
    # Create instances of Right and Left
    right1 = Right(10)
    right2 = Right(10)
    right3 = Right(20)
    left1 = Left(10)
    left2 = Left(10)
    left3 = Left(20)
    non_either = "Not an Either"

    # Test equality of the same type and value
    assert right1 == right2, "Right instances with the same value should be equal"
    assert left1 == left2, "Left instances with the same value should be equal"

    # Test inequality of different values
    assert right1 != right3, "Right instances with different values should not be equal"
    assert left1 != left3, "Left instances with different values should not be equal"

    # Test inequality of different types (Right vs Left)
    assert right1 != left1, "Right and Left instances should not be equal"

    # Test inequality with non-Either type
    assert right1 != non_either, "Either should not be equal to non-Either type"
    assert left1 != non_either, "Either should not be equal to non-Either type"
