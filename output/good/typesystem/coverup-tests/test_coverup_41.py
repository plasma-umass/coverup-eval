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

@pytest.fixture
def mock_token():
    return MockToken(content="Hello, World!", start_index=0, end_index=4)

def test_token_string_property(mock_token):
    assert mock_token.string == "Hello"
