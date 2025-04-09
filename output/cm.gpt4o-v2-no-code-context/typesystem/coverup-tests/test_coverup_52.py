# file: typesystem/tokenize/tokens.py:36-38
# asked: {"lines": [36, 37, 38], "branches": []}
# gained: {"lines": [36, 37, 38], "branches": []}

import pytest
from typesystem.tokenize.tokens import Token, Position

class MockPosition:
    def __init__(self, line, column, char_index):
        self.line = line
        self.column = column
        self.char_index = char_index

class MockToken(Token):
    def __init__(self, end_index):
        self._end_index = end_index

    def _get_position(self, index):
        return MockPosition(index, index, index)

def test_token_end_property():
    token = MockToken(5)
    end_position = token.end
    assert isinstance(end_position, MockPosition)
    assert end_position.line == 5
    assert end_position.column == 5
    assert end_position.char_index == 5
