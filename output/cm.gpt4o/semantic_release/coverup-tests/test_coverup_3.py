# file semantic_release/hvcs.py:484-490
# lines [484, 490]
# branches []

import pytest
from unittest.mock import patch
from semantic_release.hvcs import get_token, get_hvcs

@pytest.fixture
def mock_get_hvcs(mocker):
    mock_hvcs = mocker.patch('semantic_release.hvcs.get_hvcs')
    mock_hvcs.return_value.token.return_value = 'mocked_token'
    return mock_hvcs

def test_get_token(mock_get_hvcs):
    token = get_token()
    assert token == 'mocked_token'
    mock_get_hvcs.assert_called_once()
    mock_get_hvcs.return_value.token.assert_called_once()
