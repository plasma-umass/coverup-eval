# file lib/ansible/galaxy/token.py:66-93
# lines [66, 67, 68, 78, 80, 81, 82, 83, 84, 88, 91, 93]
# branches ['67->68', '67->78']

import pytest
from unittest.mock import patch, MagicMock
import json

# Assuming the KeycloakToken class is imported from ansible.galaxy.token
from ansible.galaxy.token import KeycloakToken

@pytest.fixture
def keycloak_token():
    token = KeycloakToken()
    token._token = None
    token.auth_url = "https://example.com/auth"
    token.validate_certs = True
    return token

def test_keycloak_token_get_with_token(keycloak_token):
    keycloak_token._token = "existing_token"
    assert keycloak_token.get() == "existing_token"

@patch('ansible.galaxy.token.open_url')
@patch('ansible.galaxy.token.to_native')
@patch('ansible.galaxy.token.to_text')
@patch('ansible.galaxy.token.user_agent')
def test_keycloak_token_get_without_token(mock_user_agent, mock_to_text, mock_to_native, mock_open_url, keycloak_token):
    mock_user_agent.return_value = "test-agent"
    mock_to_native.return_value = keycloak_token.auth_url
    mock_response = MagicMock()
    mock_response.read.return_value = json.dumps({'access_token': 'new_token'}).encode('utf-8')
    mock_open_url.return_value = mock_response
    mock_to_text.return_value = json.dumps({'access_token': 'new_token'})

    with patch.object(keycloak_token, '_form_payload', return_value="payload"):
        token = keycloak_token.get()
        assert token == 'new_token'
        assert keycloak_token._token == 'new_token'
        mock_open_url.assert_called_once_with(
            keycloak_token.auth_url,
            data="payload",
            validate_certs=keycloak_token.validate_certs,
            method='POST',
            http_agent="test-agent"
        )

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Add any necessary cleanup code here
