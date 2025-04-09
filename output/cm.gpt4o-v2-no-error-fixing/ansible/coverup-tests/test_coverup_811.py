# file: lib/ansible/galaxy/token.py:95-98
# asked: {"lines": [96, 97, 98], "branches": []}
# gained: {"lines": [96, 97, 98], "branches": []}

import pytest
from ansible.galaxy.token import KeycloakToken

class MockKeycloakToken(KeycloakToken):
    def get(self):
        return "mock_token"

@pytest.fixture
def mock_keycloak_token():
    return MockKeycloakToken()

def test_headers(mock_keycloak_token):
    headers = mock_keycloak_token.headers()
    assert headers['Authorization'] == 'Bearer mock_token'
