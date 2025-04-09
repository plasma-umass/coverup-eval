# file: typesystem/tokenize/tokenize_yaml.py:17-22
# asked: {"lines": [17, 18, 19, 20, 21], "branches": []}
# gained: {"lines": [17, 18, 19, 20, 21], "branches": []}

import pytest
from typesystem.base import Position
from typesystem.tokenize.tokenize_yaml import _get_position

def test_get_position_start_of_content():
    content = "line1\nline2\nline3"
    index = 0
    position = _get_position(content, index)
    assert position.line_no == 1
    assert position.column_no == 1
    assert position.char_index == 0

def test_get_position_middle_of_content():
    content = "line1\nline2\nline3"
    index = 6
    position = _get_position(content, index)
    assert position.line_no == 2
    assert position.column_no == 1
    assert position.char_index == 6

def test_get_position_end_of_content():
    content = "line1\nline2\nline3"
    index = len(content) - 1
    position = _get_position(content, index)
    assert position.line_no == 3
    assert position.column_no == 5
    assert position.char_index == len(content) - 1

def test_get_position_newline_character():
    content = "line1\nline2\nline3"
    index = content.find('\n')
    position = _get_position(content, index)
    assert position.line_no == 1
    assert position.column_no == 6
    assert position.char_index == index

def test_get_position_after_newline_character():
    content = "line1\nline2\nline3"
    index = content.find('\n') + 1
    position = _get_position(content, index)
    assert position.line_no == 2
    assert position.column_no == 1
    assert position.char_index == index
