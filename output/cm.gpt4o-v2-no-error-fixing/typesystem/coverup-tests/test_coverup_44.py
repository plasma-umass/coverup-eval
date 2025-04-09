# file: typesystem/tokenize/tokens.py:56-61
# asked: {"lines": [57, 58, 59, 60, 61], "branches": []}
# gained: {"lines": [57, 58, 59, 60, 61], "branches": []}

import pytest
from typesystem.tokenize.tokens import Token
from typesystem.base import Position

class MockToken(Token):
    def __init__(self, content):
        self._content = content

def test_get_position_single_line():
    token = MockToken("hello world")
    position = token._get_position(5)
    assert position == Position(line_no=1, column_no=6, char_index=5)

def test_get_position_multiple_lines():
    token = MockToken("hello\nworld")
    position = token._get_position(8)
    assert position == Position(line_no=2, column_no=3, char_index=8)

def test_get_position_empty_content():
    token = MockToken("")
    position = token._get_position(0)
    assert position == Position(line_no=1, column_no=1, char_index=0)
