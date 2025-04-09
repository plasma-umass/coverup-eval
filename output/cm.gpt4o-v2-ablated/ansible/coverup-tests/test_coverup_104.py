# file: lib/ansible/galaxy/token.py:66-93
# asked: {"lines": [66, 67, 68, 78, 80, 81, 82, 83, 84, 88, 91, 93], "branches": [[67, 68], [67, 78]]}
# gained: {"lines": [66, 67, 68, 78, 80, 81, 82, 83, 84, 88, 91, 93], "branches": [[67, 68], [67, 78]]}

import pytest
import json
from unittest.mock import patch, MagicMock

# Assuming the KeycloakToken class is imported from ansible/galaxy/token.py
from ansible.galaxy.token import KeycloakToken

@pytest.fixture
def keycloak_token():
    token = KeycloakToken()
    token._token = None
    token.auth_url = "https://auth.example.com"
    token.validate_certs = True
    return token

def test_get_token_cached(keycloak_token):
    keycloak_token._token = "cached_token"
    assert keycloak_token.get() == "cached_token"

@patch('ansible.galaxy.token.open_url')
@patch('ansible.galaxy.token.to_native')
@patch('ansible.galaxy.token.to_text')
@patch('ansible.galaxy.token.user_agent')
def test_get_token_new(mock_user_agent, mock_to_text, mock_to_native, mock_open_url, keycloak_token):
    mock_user_agent.return_value = "test-agent"
    mock_to_native.return_value = keycloak_token.auth_url
    mock_resp = MagicMock()
    mock_resp.read.return_value = json.dumps({'access_token': 'new_token'}).encode('utf-8')
    mock_open_url.return_value = mock_resp
    mock_to_text.return_value = mock_resp.read.return_value.decode('utf-8')

    with patch.object(keycloak_token, '_form_payload', return_value="payload"):
        token = keycloak_token.get()
        assert token == "new_token"
        assert keycloak_token._token == "new_token"
        mock_open_url.assert_called_once_with(
            keycloak_token.auth_url,
            data="payload",
            validate_certs=keycloak_token.validate_certs,
            method='POST',
            http_agent="test-agent"
        )
