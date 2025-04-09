# file: semantic_release/hvcs.py:484-490
# asked: {"lines": [484, 490], "branches": []}
# gained: {"lines": [484, 490], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from semantic_release.hvcs import get_token, get_hvcs, Github, Gitlab
from semantic_release.errors import ImproperConfigurationError

@pytest.fixture
def mock_get_hvcs():
    with patch('semantic_release.hvcs.get_hvcs') as mock:
        yield mock

def test_get_token_valid_token(mock_get_hvcs):
    mock_hvcs_instance = MagicMock()
    mock_hvcs_instance.token.return_value = 'valid_token'
    mock_get_hvcs.return_value = mock_hvcs_instance

    token = get_token()
    assert token == 'valid_token'

def test_get_token_no_token(mock_get_hvcs):
    mock_hvcs_instance = MagicMock()
    mock_hvcs_instance.token.return_value = None
    mock_get_hvcs.return_value = mock_hvcs_instance

    token = get_token()
    assert token is None

def test_get_hvcs_valid():
    with patch('semantic_release.hvcs.config.get') as mock_config_get:
        mock_config_get.return_value = 'Github'
        with patch('semantic_release.hvcs.Github', new=MagicMock()):
            hvcs_instance = get_hvcs()
            assert hvcs_instance is not None

    with patch('semantic_release.hvcs.config.get') as mock_config_get:
        mock_config_get.return_value = 'Gitlab'
        with patch('semantic_release.hvcs.Gitlab', new=MagicMock()):
            hvcs_instance = get_hvcs()
            assert hvcs_instance is not None

def test_get_hvcs_invalid():
    with patch('semantic_release.hvcs.config.get') as mock_config_get:
        mock_config_get.return_value = 'InvalidHvcs'
        with pytest.raises(ImproperConfigurationError):
            get_hvcs()
