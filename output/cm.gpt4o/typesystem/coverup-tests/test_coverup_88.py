# file typesystem/tokenize/tokens.py:49-54
# lines [53, 54]
# branches []

import pytest
from typesystem.tokenize.tokens import Token

class MockToken(Token):
    def __init__(self, value=None, start_index=None, end_index=None):
        super().__init__(value, start_index, end_index)

    def lookup(self, index):
        # Mock implementation of lookup to return self for testing purposes
        return self

    def _get_key_token(self, key):
        # Mock implementation of _get_key_token to return a new token for testing purposes
        return Token(value=key, start_index=0, end_index=0)

def test_lookup_key(mocker):
    mock_token = MockToken(value="test", start_index=0, end_index=0)
    index = [1, 2, 3]

    # Mock the lookup method to ensure it returns the mock_token itself
    mocker.patch.object(mock_token, 'lookup', return_value=mock_token)
    # Mock the _get_key_token method to ensure it returns a new Token instance
    mocker.patch.object(mock_token, '_get_key_token', return_value=Token(value="key", start_index=0, end_index=0))

    result = mock_token.lookup_key(index)

    # Assertions to verify the correct behavior
    mock_token.lookup.assert_called_once_with(index[:-1])
    mock_token._get_key_token.assert_called_once_with(index[-1])
    assert isinstance(result, Token)
