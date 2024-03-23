# file lib/ansible/galaxy/token.py:142-144
# lines [142, 143, 144]
# branches []

import pytest
from ansible.galaxy.token import GalaxyToken

@pytest.fixture
def galaxy_token(mocker):
    # Mock the save method to avoid any side effects
    mocker.patch.object(GalaxyToken, 'save', return_value=None)
    return GalaxyToken()

def test_galaxy_token_set(galaxy_token):
    test_token = 'test_token'
    galaxy_token.set(test_token)
    assert galaxy_token._token == test_token, "Token was not set correctly"
