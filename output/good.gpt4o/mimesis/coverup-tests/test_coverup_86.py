# file mimesis/providers/cryptographic.py:104-117
# lines [104, 105, 117]
# branches []

import pytest
from mimesis.providers.cryptographic import Cryptographic

def test_token_urlsafe(mocker):
    # Mock the secrets.token_urlsafe function to control its output
    mock_token_urlsafe = mocker.patch('secrets.token_urlsafe', return_value='mocked_token')

    # Create an instance of the Cryptographic provider
    crypto_provider = Cryptographic()

    # Test with default entropy
    token = crypto_provider.token_urlsafe()
    assert token == 'mocked_token'
    mock_token_urlsafe.assert_called_once_with(32)

    # Test with specific entropy
    token = crypto_provider.token_urlsafe(64)
    assert token == 'mocked_token'
    mock_token_urlsafe.assert_called_with(64)
