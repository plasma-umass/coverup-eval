# file lib/ansible/galaxy/token.py:142-144
# lines [142, 143, 144]
# branches []

import pytest
from unittest.mock import patch

# Assuming the GalaxyToken class is imported from ansible.galaxy.token
from ansible.galaxy.token import GalaxyToken

@pytest.fixture
def galaxy_token():
    return GalaxyToken()

def test_set_token(galaxy_token, mocker):
    mock_save = mocker.patch.object(galaxy_token, 'save')
    
    test_token = "test_token_value"
    galaxy_token.set(test_token)
    
    assert galaxy_token._token == test_token
    mock_save.assert_called_once()
