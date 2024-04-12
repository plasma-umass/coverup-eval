# file typesystem/tokenize/tokens.py:7-13
# lines [7, 8, 10, 11, 12, 13]
# branches []

import pytest
from typesystem.tokenize.tokens import Token

def test_token_initialization():
    # Initialize a token with some values
    value = "test_value"
    start_index = 0
    end_index = 10
    content = "test_content"
    
    # Create a token instance
    token = Token(value, start_index, end_index, content)
    
    # Assert that the token properties are correctly assigned
    assert token._value == value
    assert token._start_index == start_index
    assert token._end_index == end_index
    assert token._content == content

    # Clean up is not necessary as no external resources are being modified
