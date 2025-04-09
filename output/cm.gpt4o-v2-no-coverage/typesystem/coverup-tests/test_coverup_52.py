# file: typesystem/tokenize/tokens.py:32-34
# asked: {"lines": [32, 33, 34], "branches": []}
# gained: {"lines": [32, 33, 34], "branches": []}

import pytest
from typesystem.tokenize.tokens import Token
from typesystem.base import Position

def test_token_start():
    token = Token(value="test", start_index=5, end_index=10, content="test content")
    
    # Mock the _get_position method to return a known Position
    def mock_get_position(index):
        return Position(line_no=1, column_no=index, char_index=index)
    
    token._get_position = mock_get_position
    
    start_position = token.start
    
    assert isinstance(start_position, Position)
    assert start_position.line_no == 1
    assert start_position.column_no == 5
    assert start_position.char_index == 5
