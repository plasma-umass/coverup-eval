# file: lib/ansible/galaxy/token.py:66-93
# asked: {"lines": [66, 67, 68, 78, 80, 81, 82, 83, 84, 88, 91, 93], "branches": [[67, 68], [67, 78]]}
# gained: {"lines": [66, 67, 68, 78, 80, 81, 82, 83, 84, 88, 91, 93], "branches": [[67, 68], [67, 78]]}

import pytest
import json
from unittest.mock import patch, MagicMock
from ansible.galaxy.token import KeycloakToken

@pytest.fixture
def keycloak_token():
    token = KeycloakToken()
    token._token = None
    token.auth_url = "https://auth.example.com"
    token.validate_certs = False
    token.client_id = "cloud-services"
    token.access_token = "dummy_refresh_token"
    return token

def test_get_token_from_cache(keycloak_token):
    keycloak_token._token = "cached_token"
    assert keycloak_token.get() == "cached_token"

@patch('ansible.galaxy.token.open_url')
def test_get_token_from_server(mock_open_url, keycloak_token):
    mock_response = MagicMock()
    mock_response.read.return_value = json.dumps({"access_token": "new_token"}).encode('utf-8')
    mock_open_url.return_value = mock_response

    token = keycloak_token.get()
    assert token == "new_token"
    assert keycloak_token._token == "new_token"

def test_form_payload(keycloak_token):
    payload = keycloak_token._form_payload()
    expected_payload = 'grant_type=refresh_token&client_id=cloud-services&refresh_token=dummy_refresh_token'
    assert payload == expected_payload
