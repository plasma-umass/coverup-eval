# file: lib/ansible/galaxy/token.py:112-121
# asked: {"lines": [112, 113, 114, 115, 118, 119, 121], "branches": [[114, 115], [114, 118], [118, 119], [118, 121]]}
# gained: {"lines": [112, 113, 114, 115, 118, 119, 121], "branches": [[114, 115], [118, 119], [118, 121]]}

import pytest
from ansible.galaxy.token import GalaxyToken, NoTokenSentinel

@pytest.fixture
def galaxy_token():
    return GalaxyToken()

def test_config_reads_and_sets_token(galaxy_token, mocker):
    mocker.patch.object(galaxy_token, '_read', return_value={'token': 'existing_token'})
    galaxy_token._token = 'new_token'
    config = galaxy_token.config
    assert config['token'] == 'new_token'

def test_config_reads_and_sets_no_token_sentinel(galaxy_token, mocker):
    mocker.patch.object(galaxy_token, '_read', return_value={'token': 'existing_token'})
    galaxy_token._token = NoTokenSentinel
    config = galaxy_token.config
    assert config['token'] is None

def test_config_reads_without_token(galaxy_token, mocker):
    mocker.patch.object(galaxy_token, '_read', return_value={'token': 'existing_token'})
    galaxy_token._token = None
    config = galaxy_token.config
    assert config['token'] == 'existing_token'
