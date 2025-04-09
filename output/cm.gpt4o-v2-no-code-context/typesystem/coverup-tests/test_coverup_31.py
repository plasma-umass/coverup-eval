# file: typesystem/tokenize/tokenize_yaml.py:17-22
# asked: {"lines": [17, 18, 19, 20, 21], "branches": []}
# gained: {"lines": [17, 18, 19, 20, 21], "branches": []}

import pytest
from typesystem.tokenize.tokenize_yaml import _get_position, Position

def test_get_position_start_of_content():
    content = "line1\nline2\nline3"
    index = 0
    position = _get_position(content, index)
    assert position == Position(line_no=1, column_no=1, char_index=0)

def test_get_position_middle_of_content():
    content = "line1\nline2\nline3"
    index = 6
    position = _get_position(content, index)
    assert position == Position(line_no=2, column_no=1, char_index=6)

def test_get_position_end_of_content():
    content = "line1\nline2\nline3"
    index = len(content) - 1
    position = _get_position(content, index)
    assert position == Position(line_no=3, column_no=5, char_index=index)
