# file: lib/ansible/galaxy/token.py:142-144
# asked: {"lines": [142, 143, 144], "branches": []}
# gained: {"lines": [142, 143, 144], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.galaxy.token import GalaxyToken

@pytest.fixture
def galaxy_token():
    return GalaxyToken()

def test_set_method(galaxy_token, mocker):
    mock_save = mocker.patch.object(galaxy_token, 'save')
    token_value = "test_token"
    
    galaxy_token.set(token_value)
    
    assert galaxy_token._token == token_value
    mock_save.assert_called_once()
