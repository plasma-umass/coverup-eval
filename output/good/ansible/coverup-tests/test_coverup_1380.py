# file lib/ansible/galaxy/token.py:95-98
# lines [96, 97, 98]
# branches []

import pytest
from ansible.galaxy.token import KeycloakToken

@pytest.fixture
def keycloak_token(mocker):
    mocker.patch.object(KeycloakToken, 'get', return_value='dummy_token')
    mocker.patch.object(KeycloakToken, 'token_type', new_callable=mocker.PropertyMock(return_value='Bearer'))
    return KeycloakToken()

def test_keycloak_token_headers(keycloak_token):
    expected_headers = {
        'Authorization': 'Bearer dummy_token'
    }
    headers = keycloak_token.headers()
    assert headers == expected_headers
