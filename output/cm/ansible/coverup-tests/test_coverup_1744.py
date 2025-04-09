# file lib/ansible/galaxy/token.py:146-147
# lines [147]
# branches []

import pytest
from ansible.galaxy.token import GalaxyToken

@pytest.fixture
def galaxy_token(mocker):
    # Mock the config attribute to simulate the presence of a configuration
    config_mock = mocker.MagicMock()
    config_mock.get.return_value = 'test_token'
    mocker.patch.object(GalaxyToken, 'config', config_mock)
    return GalaxyToken()

def test_galaxy_token_get(galaxy_token):
    # Test the get method to ensure it retrieves the token correctly
    token = galaxy_token.get()
    assert token == 'test_token', "The token should be retrieved from the config"

def test_galaxy_token_get_no_token(galaxy_token, mocker):
    # Modify the mock to simulate the absence of a token in the configuration
    config_mock = mocker.MagicMock()
    config_mock.get.return_value = None
    mocker.patch.object(GalaxyToken, 'config', config_mock)
    token = galaxy_token.get()
    assert token is None, "The token should be None when not present in the config"
