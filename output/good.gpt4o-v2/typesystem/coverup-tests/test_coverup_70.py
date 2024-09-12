# file: typesystem/tokenize/tokens.py:36-38
# asked: {"lines": [36, 37, 38], "branches": []}
# gained: {"lines": [36, 37, 38], "branches": []}

import pytest
from typesystem.tokenize.tokens import Token
from typesystem.base import Position

def test_token_end():
    # Arrange
    value = "test"
    start_index = 0
    end_index = 5
    content = "test content"
    
    token = Token(value, start_index, end_index, content)
    
    # Mock the _get_position method to return a specific Position
    def mock_get_position(index):
        return Position(line_no=1, column_no=index, char_index=index)
    
    token._get_position = mock_get_position
    
    # Act
    end_position = token.end
    
    # Assert
    assert end_position == Position(line_no=1, column_no=end_index, char_index=end_index)
