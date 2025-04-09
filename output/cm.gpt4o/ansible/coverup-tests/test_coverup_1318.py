# file lib/ansible/galaxy/token.py:146-147
# lines [147]
# branches []

import pytest
from unittest.mock import MagicMock, patch

# Assuming the GalaxyToken class is imported from ansible.galaxy.token
from ansible.galaxy.token import GalaxyToken

@pytest.fixture
def mock_config():
    return MagicMock()

@pytest.fixture
def galaxy_token(mock_config):
    with patch.object(GalaxyToken, 'config', new_callable=MagicMock) as mock_config_attr:
        mock_config_attr.get = mock_config.get
        token_instance = GalaxyToken()
        yield token_instance

def test_get_token_present(galaxy_token, mock_config):
    mock_config.get.return_value = 'test_token'
    token = galaxy_token.get()
    assert token == 'test_token'
    mock_config.get.assert_called_once_with('token', None)

def test_get_token_absent(galaxy_token, mock_config):
    mock_config.get.return_value = None
    token = galaxy_token.get()
    assert token is None
    mock_config.get.assert_called_once_with('token', None)
