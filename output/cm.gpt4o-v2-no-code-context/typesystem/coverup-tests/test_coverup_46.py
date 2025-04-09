# file: typesystem/tokenize/tokens.py:49-54
# asked: {"lines": [49, 53, 54], "branches": []}
# gained: {"lines": [49, 53, 54], "branches": []}

import pytest
from typesystem.tokenize.tokens import Token

class MockToken(Token):
    def __init__(self, value, start_index, end_index):
        super().__init__(value, start_index, end_index)

    def lookup(self, index):
        # Mock implementation of lookup method
        return self

    def _get_key_token(self, key):
        # Mock implementation of _get_key_token method
        return f"Token for key: {key}"

@pytest.fixture
def mock_token():
    return MockToken(value="mock_value", start_index=0, end_index=1)

def test_lookup_key(mock_token):
    index = [1, 2, 3]
    result = mock_token.lookup_key(index)
    assert result == "Token for key: 3"

def test_lookup_key_empty_index(mock_token):
    index = []
    with pytest.raises(IndexError):
        mock_token.lookup_key(index)
