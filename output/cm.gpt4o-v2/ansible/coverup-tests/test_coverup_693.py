# file: lib/ansible/galaxy/token.py:95-98
# asked: {"lines": [95, 96, 97, 98], "branches": []}
# gained: {"lines": [95, 96, 97, 98], "branches": []}

import pytest
from unittest.mock import patch, Mock
from ansible.galaxy.token import KeycloakToken

@pytest.fixture
def keycloak_token():
    return KeycloakToken(access_token="dummy_access_token", auth_url="http://dummy_url")

def test_headers(keycloak_token):
    with patch.object(KeycloakToken, 'get', return_value="dummy_token"):
        headers = keycloak_token.headers()
        assert headers['Authorization'] == 'Bearer dummy_token'
