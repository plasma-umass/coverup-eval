# file typesystem/tokenize/tokenize_yaml.py:17-22
# lines [17, 18, 19, 20, 21]
# branches []

import pytest
from typesystem.tokenize.tokenize_yaml import _get_position, Position

def test_get_position():
    content = "line1\nline2\nline3"
    index = 12  # This should be in the middle of "line3"
    
    position = _get_position(content, index)
    
    assert position.line_no == 3
    assert position.column_no == index - content.rfind("\n", 0, index)
    assert position.char_index == index
