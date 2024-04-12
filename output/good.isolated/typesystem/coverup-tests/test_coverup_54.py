# file typesystem/tokenize/tokens.py:49-54
# lines [49, 53, 54]
# branches []

import pytest
from typesystem.tokenize.tokens import Token

class MockToken(Token):
    def __init__(self, value=None, start_index=None, end_index=None):
        super().__init__(value, start_index, end_index)

    def lookup(self, index):
        # Mock the lookup method to return a token with a _get_key_token method
        mock_token = MockToken()
        mock_token._get_key_token = lambda key: f"key_token_{key}"
        return mock_token

@pytest.fixture
def mock_token():
    return MockToken(value='', start_index=0, end_index=0)

def test_lookup_key(mock_token):
    index = [1, 'key']
    expected_key_token = "key_token_key"
    key_token = mock_token.lookup_key(index)
    assert key_token == expected_key_token
