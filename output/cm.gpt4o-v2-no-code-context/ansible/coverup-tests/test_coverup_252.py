# file: lib/ansible/galaxy/token.py:66-93
# asked: {"lines": [66, 67, 68, 78, 80, 81, 82, 83, 84, 88, 91, 93], "branches": [[67, 68], [67, 78]]}
# gained: {"lines": [66, 67, 68, 78, 80, 81, 82, 83, 84, 88, 91, 93], "branches": [[67, 68], [67, 78]]}

import pytest
from unittest.mock import patch, MagicMock
import json

# Assuming the KeycloakToken class is imported from ansible.galaxy.token
from ansible.galaxy.token import KeycloakToken

@pytest.fixture
def keycloak_token():
    return KeycloakToken()

def test_get_token_from_cache(keycloak_token):
    keycloak_token._token = 'cached_token'
    assert keycloak_token.get() == 'cached_token'

@patch('ansible.galaxy.token.open_url')
@patch('ansible.galaxy.token.to_native')
@patch('ansible.galaxy.token.to_text')
@patch('ansible.galaxy.token.user_agent')
def test_get_token_from_server(mock_user_agent, mock_to_text, mock_to_native, mock_open_url, keycloak_token):
    keycloak_token._token = None
    keycloak_token.auth_url = 'http://auth.url'
    keycloak_token.validate_certs = True

    mock_to_native.return_value = 'http://auth.url'
    mock_user_agent.return_value = 'user-agent'
    
    mock_response = MagicMock()
    mock_response.read.return_value = json.dumps({'access_token': 'new_token'}).encode('utf-8')
    mock_open_url.return_value = mock_response
    mock_to_text.return_value = json.dumps({'access_token': 'new_token'})

    with patch.object(keycloak_token, '_form_payload', return_value='payload'):
        token = keycloak_token.get()
    
    assert token == 'new_token'
    assert keycloak_token._token == 'new_token'
    mock_open_url.assert_called_once_with('http://auth.url', data='payload', validate_certs=True, method='POST', http_agent='user-agent')
    mock_to_text.assert_called_once_with(mock_response.read(), errors='surrogate_or_strict')
