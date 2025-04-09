# file: semantic_release/hvcs.py:484-490
# asked: {"lines": [484, 490], "branches": []}
# gained: {"lines": [484, 490], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from semantic_release.hvcs import get_token, get_hvcs
from semantic_release.errors import ImproperConfigurationError

@pytest.fixture
def mock_get_hvcs():
    with patch('semantic_release.hvcs.get_hvcs') as mock:
        yield mock

def test_get_token_success(mock_get_hvcs):
    mock_hvcs_instance = MagicMock()
    mock_hvcs_instance.token.return_value = 'fake_token'
    mock_get_hvcs.return_value = mock_hvcs_instance

    token = get_token()
    assert token == 'fake_token'
    mock_get_hvcs.assert_called_once()
    mock_hvcs_instance.token.assert_called_once()

def test_get_token_improper_configuration(mock_get_hvcs):
    mock_get_hvcs.side_effect = ImproperConfigurationError

    with pytest.raises(ImproperConfigurationError):
        get_token()
    mock_get_hvcs.assert_called_once()
