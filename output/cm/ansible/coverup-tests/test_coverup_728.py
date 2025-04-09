# file lib/ansible/galaxy/token.py:62-64
# lines [62, 63, 64]
# branches []

import pytest
from ansible.galaxy.token import KeycloakToken

@pytest.fixture
def keycloak_token():
    token = KeycloakToken()
    token.client_id = 'test_client_id'
    token.access_token = 'test_access_token'
    return token

def test_form_payload(keycloak_token):
    expected_payload = 'grant_type=refresh_token&client_id=test_client_id&refresh_token=test_access_token'
    assert keycloak_token._form_payload() == expected_payload
