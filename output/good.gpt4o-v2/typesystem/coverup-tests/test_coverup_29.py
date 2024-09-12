# file: typesystem/tokenize/tokens.py:56-61
# asked: {"lines": [56, 57, 58, 59, 60, 61], "branches": []}
# gained: {"lines": [56, 57, 58, 59, 60, 61], "branches": []}

import pytest
from typesystem.tokenize.tokens import Token
from typesystem.base import Position

class MockToken(Token):
    def __init__(self, content):
        self._content = content

def test_get_position_single_line():
    token = MockToken("Hello, World!")
    position = token._get_position(5)
    assert position == Position(1, 6, 5)

def test_get_position_multiple_lines():
    token = MockToken("Hello,\nWorld!")
    position = token._get_position(7)
    assert position == Position(2, 1, 7)

def test_get_position_empty_content():
    token = MockToken("")
    position = token._get_position(0)
    assert position == Position(1, 1, 0)

def test_get_position_end_of_content():
    token = MockToken("Hello,\nWorld!")
    position = token._get_position(12)
    assert position == Position(2, 6, 12)
