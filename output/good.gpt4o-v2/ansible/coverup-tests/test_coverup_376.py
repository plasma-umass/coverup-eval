# file: lib/ansible/galaxy/token.py:112-121
# asked: {"lines": [112, 113, 114, 115, 118, 119, 121], "branches": [[114, 115], [114, 118], [118, 119], [118, 121]]}
# gained: {"lines": [112, 113, 114, 115, 118, 119, 121], "branches": [[114, 115], [118, 119], [118, 121]]}

import pytest
from ansible.galaxy.token import GalaxyToken, NoTokenSentinel

class MockConfig:
    def __init__(self):
        self._config = None

    def _read(self):
        return {'token': 'existing_token'}

def test_config_with_no_token(mocker):
    mocker.patch('ansible.galaxy.token.GalaxyToken._read', return_value={'token': 'existing_token'})
    token_instance = GalaxyToken()
    config = token_instance.config
    assert config['token'] == 'existing_token'

def test_config_with_token(mocker):
    mocker.patch('ansible.galaxy.token.GalaxyToken._read', return_value={'token': 'existing_token'})
    token_instance = GalaxyToken(token='new_token')
    config = token_instance.config
    assert config['token'] == 'new_token'

def test_config_with_no_token_sentinel(mocker):
    mocker.patch('ansible.galaxy.token.GalaxyToken._read', return_value={'token': 'existing_token'})
    token_instance = GalaxyToken(token=NoTokenSentinel)
    config = token_instance.config
    assert config['token'] is None
