# file: semantic_release/hvcs.py:484-490
# asked: {"lines": [484, 490], "branches": []}
# gained: {"lines": [484, 490], "branches": []}

import pytest
from unittest.mock import patch
from semantic_release.hvcs import get_token, get_hvcs

@pytest.fixture
def mock_get_hvcs(mocker):
    mock_hvcs = mocker.Mock()
    mock_hvcs.token.return_value = "fake_token"
    mocker.patch("semantic_release.hvcs.get_hvcs", return_value=mock_hvcs)
    return mock_hvcs

def test_get_token_returns_token(mock_get_hvcs):
    token = get_token()
    assert token == "fake_token"
    mock_get_hvcs.token.assert_called_once()

def test_get_token_no_token(mocker):
    mock_hvcs = mocker.Mock()
    mock_hvcs.token.return_value = None
    mocker.patch("semantic_release.hvcs.get_hvcs", return_value=mock_hvcs)
    
    token = get_token()
    assert token is None
    mock_hvcs.token.assert_called_once()
