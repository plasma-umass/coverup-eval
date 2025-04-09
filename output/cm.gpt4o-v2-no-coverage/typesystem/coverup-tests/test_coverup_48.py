# file: typesystem/tokenize/tokens.py:36-38
# asked: {"lines": [36, 37, 38], "branches": []}
# gained: {"lines": [36, 37, 38], "branches": []}

import pytest
from typesystem.base import Position
from typesystem.tokenize.tokens import Token

class MockToken(Token):
    def __init__(self, end_index):
        self._end_index = end_index

    def _get_position(self, index):
        return Position(line_no=index, column_no=index, char_index=index)

def test_token_end():
    token = MockToken(end_index=5)
    end_position = token.end
    assert isinstance(end_position, Position)
    assert end_position.line_no == 5
    assert end_position.column_no == 5
    assert end_position.char_index == 5
