# file typesystem/base.py:5-21
# lines [5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 19, 20, 21]
# branches []

import pytest
from typesystem.base import Position

def test_position_equality():
    pos1 = Position(1, 2, 3)
    pos2 = Position(1, 2, 3)
    pos3 = Position(1, 2, 4)
    pos4 = Position(2, 2, 3)
    pos5 = Position(1, 3, 3)
    pos6 = "not a position"

    assert pos1 == pos2, "Positions with same values should be equal"
    assert pos1 != pos3, "Positions with different char_index should not be equal"
    assert pos1 != pos4, "Positions with different line_no should not be equal"
    assert pos1 != pos5, "Positions with different column_no should not be equal"
    assert pos1 != pos6, "Position should not be equal to a different type"

def test_position_repr():
    pos = Position(1, 2, 3)
    expected_repr = "Position(line_no=1, column_no=2, char_index=3)"
    assert repr(pos) == expected_repr, "Position __repr__ should match the expected format"
