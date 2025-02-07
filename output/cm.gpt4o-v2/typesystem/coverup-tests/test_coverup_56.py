# file: typesystem/tokenize/tokenize_yaml.py:17-22
# asked: {"lines": [17, 18, 19, 20, 21], "branches": []}
# gained: {"lines": [17, 18, 19, 20, 21], "branches": []}

import pytest
from typesystem.tokenize.tokenize_yaml import _get_position
from typesystem.base import Position

def test_get_position():
    content = "line1\nline2\nline3"
    index = 12  # This is the index of '\n' after "line2"
    
    expected_position = Position(line_no=3, column_no=1, char_index=12)
    actual_position = _get_position(content, index)
    
    assert actual_position == expected_position
