# file: lib/ansible/galaxy/token.py:62-64
# asked: {"lines": [62, 63, 64], "branches": []}
# gained: {"lines": [62, 63, 64], "branches": []}

import pytest
from ansible.galaxy.token import KeycloakToken

def test_keycloak_token_form_payload():
    client_id = "test_client_id"
    access_token = "test_access_token"
    token = KeycloakToken(client_id=client_id, access_token=access_token)
    
    expected_payload = 'grant_type=refresh_token&client_id=test_client_id&refresh_token=test_access_token'
    assert token._form_payload() == expected_payload

    # Clean up
    del token

@pytest.fixture
def mock_keycloak_token(monkeypatch):
    def mock_init(self, access_token=None, auth_url=None, validate_certs=True, client_id=None):
        self.access_token = access_token
        self.auth_url = auth_url
        self._token = None
        self.validate_certs = validate_certs
        self.client_id = client_id
        if self.client_id is None:
            self.client_id = 'cloud-services'
    
    monkeypatch.setattr(KeycloakToken, "__init__", mock_init)

def test_keycloak_token_form_payload_with_fixture(mock_keycloak_token):
    client_id = "fixture_client_id"
    access_token = "fixture_access_token"
    token = KeycloakToken(client_id=client_id, access_token=access_token)
    
    expected_payload = 'grant_type=refresh_token&client_id=fixture_client_id&refresh_token=fixture_access_token'
    assert token._form_payload() == expected_payload

    # Clean up
    del token
