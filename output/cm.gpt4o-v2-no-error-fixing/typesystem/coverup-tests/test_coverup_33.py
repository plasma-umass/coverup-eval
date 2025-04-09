# file: typesystem/tokenize/tokens.py:24-26
# asked: {"lines": [24, 25, 26], "branches": []}
# gained: {"lines": [24, 25, 26], "branches": []}

import pytest
from typesystem.tokenize.tokens import Token

def test_token_string_property():
    # Arrange
    content = "Hello, World!"
    start_index = 7
    end_index = 11
    token = Token(value=None, start_index=start_index, end_index=end_index, content=content)
    
    # Act
    result = token.string
    
    # Assert
    assert result == "World"

