# file typesystem/tokenize/tokens.py:24-26
# lines [24, 25, 26]
# branches []

import pytest
from typesystem.tokenize.tokens import Token

class MockToken(Token):
    def __init__(self, content, start_index, end_index):
        self._content = content
        self._start_index = start_index
        self._end_index = end_index

def test_token_string_property():
    content = "example"
    start_index = 1
    end_index = 4
    token = MockToken(content, start_index, end_index)
    
    assert token.string == "xamp"

    # Clean up
    del token
