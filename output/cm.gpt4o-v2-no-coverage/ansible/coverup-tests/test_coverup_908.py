# file: lib/ansible/galaxy/token.py:146-147
# asked: {"lines": [146, 147], "branches": []}
# gained: {"lines": [146, 147], "branches": []}

import pytest
from unittest.mock import MagicMock

from ansible.galaxy.token import GalaxyToken

@pytest.fixture
def mock_config(monkeypatch):
    mock_config = MagicMock()
    monkeypatch.setattr(GalaxyToken, 'config', mock_config)
    return mock_config

def test_get_token_exists(mock_config):
    token_instance = GalaxyToken()
    mock_config.get.return_value = 'test_token'
    
    result = token_instance.get()
    
    assert result == 'test_token'
    mock_config.get.assert_called_once_with('token', None)

def test_get_token_not_exists(mock_config):
    token_instance = GalaxyToken()
    mock_config.get.return_value = None
    
    result = token_instance.get()
    
    assert result is None
    mock_config.get.assert_called_once_with('token', None)
