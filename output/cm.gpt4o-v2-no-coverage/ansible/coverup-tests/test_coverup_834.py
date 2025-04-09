# file: lib/ansible/galaxy/token.py:142-144
# asked: {"lines": [142, 143, 144], "branches": []}
# gained: {"lines": [142, 143, 144], "branches": []}

import pytest
from unittest.mock import mock_open, patch
from ansible.galaxy.token import GalaxyToken

@pytest.fixture
def galaxy_token():
    token = GalaxyToken()
    token.b_file = 'test_file.yaml'
    token._config = {'token': 'initial'}
    return token

def test_set_token(galaxy_token):
    new_token = 'new_token_value'
    
    with patch('ansible.galaxy.token.yaml_dump') as mock_yaml_dump, \
         patch('builtins.open', mock_open()) as mock_file:
        
        galaxy_token.set(new_token)
        
        assert galaxy_token._token == new_token
        mock_yaml_dump.assert_called_once_with(galaxy_token.config, mock_file(), default_flow_style=False)
        mock_file.assert_any_call('test_file.yaml', 'w')
