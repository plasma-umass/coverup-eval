# file: lib/ansible/galaxy/token.py:146-147
# asked: {"lines": [146, 147], "branches": []}
# gained: {"lines": [146, 147], "branches": []}

import pytest
from unittest.mock import MagicMock

from ansible.galaxy.token import GalaxyToken

@pytest.fixture
def galaxy_token():
    return GalaxyToken()

def test_get_token(galaxy_token, monkeypatch):
    mock_config = {'token': 'test_token'}
    monkeypatch.setattr(galaxy_token, '_config', mock_config)
    
    token = galaxy_token.get()
    
    assert token == 'test_token'
