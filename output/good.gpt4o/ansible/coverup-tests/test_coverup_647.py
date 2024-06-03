# file lib/ansible/galaxy/token.py:95-98
# lines [95, 96, 97, 98]
# branches []

import pytest
from unittest.mock import patch

# Assuming the KeycloakToken class is imported from ansible.galaxy.token
from ansible.galaxy.token import KeycloakToken

@pytest.fixture
def keycloak_token():
    token = KeycloakToken()
    token.token_type = 'Bearer'
    return token

def test_keycloak_token_headers(keycloak_token, mocker):
    mock_get = mocker.patch.object(KeycloakToken, 'get', return_value='mocked_token')
    
    headers = keycloak_token.headers()
    
    assert headers['Authorization'] == 'Bearer mocked_token'
    mock_get.assert_called_once()

