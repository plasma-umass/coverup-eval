# file semantic_release/hvcs.py:484-490
# lines [484, 490]
# branches []

import pytest
from semantic_release.hvcs import get_hvcs
from unittest.mock import MagicMock

# Assuming the get_hvcs function returns an object with a token method
# We will mock this behavior to ensure that the get_token function is tested

@pytest.fixture
def mock_hvcs(mocker):
    mock = MagicMock()
    mock.token.return_value = 'test-token'
    mocker.patch('semantic_release.hvcs.get_hvcs', return_value=mock)
    return mock

def test_get_token(mock_hvcs):
    from semantic_release.hvcs import get_token

    # Call the function to test
    token = get_token()

    # Assert that the token method was called
    mock_hvcs.token.assert_called_once()

    # Assert that the token returned is correct
    assert token == 'test-token'
