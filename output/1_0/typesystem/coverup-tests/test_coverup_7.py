# file typesystem/base.py:5-21
# lines [5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 19, 20, 21]
# branches []

import pytest
from typesystem.base import Position

def test_position_eq():
    pos1 = Position(1, 1, 0)
    pos2 = Position(1, 1, 0)
    pos3 = Position(2, 1, 0)
    pos4 = "not_a_position"

    assert pos1 == pos2, "Positions with the same line_no, column_no, and char_index should be equal"
    assert not (pos1 == pos3), "Positions with different line_no, column_no, or char_index should not be equal"
    assert not (pos1 == pos4), "Position should not be equal to a non-Position type"

def test_position_repr():
    pos = Position(1, 1, 0)
    expected_repr = "Position(line_no=1, column_no=1, char_index=0)"
    assert repr(pos) == expected_repr, "The __repr__ method should return the expected string representation"
