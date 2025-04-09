# file: typesystem/base.py:5-21
# asked: {"lines": [5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 19, 20, 21], "branches": []}
# gained: {"lines": [5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 19, 20, 21], "branches": []}

import pytest
from typesystem.base import Position

def test_position_init():
    pos = Position(1, 2, 3)
    assert pos.line_no == 1
    assert pos.column_no == 2
    assert pos.char_index == 3

def test_position_eq():
    pos1 = Position(1, 2, 3)
    pos2 = Position(1, 2, 3)
    pos3 = Position(4, 5, 6)
    assert pos1 == pos2
    assert pos1 != pos3
    assert pos1 != "not a position"

def test_position_repr():
    pos = Position(1, 2, 3)
    assert repr(pos) == "Position(line_no=1, column_no=2, char_index=3)"
