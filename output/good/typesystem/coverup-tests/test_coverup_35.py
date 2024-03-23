# file typesystem/tokenize/tokenize_yaml.py:17-22
# lines [17, 18, 19, 20, 21]
# branches []

import pytest
from typesystem.tokenize.tokenize_yaml import _get_position, Position

def test_get_position():
    content = "line 1\nline 2\nline 3"
    index = content.find("line 2")
    expected_position = Position(line_no=2, column_no=1, char_index=index)
    
    position = _get_position(content, index)
    
    assert position == expected_position, "The position does not match the expected value."

    # Test end of file without newline
    index = len(content)
    expected_position = Position(line_no=3, column_no=7, char_index=index)
    
    position = _get_position(content, index)
    
    assert position == expected_position, "The position at the end of file without newline does not match the expected value."

    # Test start of file
    index = 0
    expected_position = Position(line_no=1, column_no=1, char_index=index)
    
    position = _get_position(content, index)
    
    assert position == expected_position, "The position at the start of file does not match the expected value."

    # Test empty content
    content = ""
    index = 0
    expected_position = Position(line_no=1, column_no=1, char_index=index)
    
    position = _get_position(content, index)
    
    assert position == expected_position, "The position for empty content does not match the expected value."

    # Test content with only newlines
    content = "\n\n\n"
    index = content.rfind("\n")
    expected_position = Position(line_no=3, column_no=1, char_index=index)
    
    position = _get_position(content, index)
    
    assert position == expected_position, "The position for content with only newlines does not match the expected value."

# Note: The actual module path for _get_position and Position should be adjusted based on the real project structure.
