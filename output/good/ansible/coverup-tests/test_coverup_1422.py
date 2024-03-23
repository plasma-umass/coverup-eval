# file lib/ansible/galaxy/token.py:66-93
# lines [68]
# branches ['67->68']

import pytest
from ansible.galaxy.token import KeycloakToken
from unittest.mock import MagicMock

@pytest.fixture
def keycloak_token():
    token = KeycloakToken()
    token._token = None
    token.auth_url = "http://auth.url"
    token.validate_certs = True
    token._form_payload = MagicMock(return_value="payload")
    return token

@pytest.fixture
def mocked_open_url(mocker):
    mocked_response = MagicMock()
    mocked_response.read.return_value = '{"access_token": "test_access_token"}'.encode('utf-8')
    mocker.patch('ansible.galaxy.token.open_url', return_value=mocked_response)
    mocker.patch('ansible.galaxy.token.to_native', side_effect=lambda x: x)
    mocker.patch('ansible.galaxy.token.to_text', side_effect=lambda x, errors: x.decode('utf-8'))
    mocker.patch('ansible.galaxy.token.user_agent', return_value="test_agent")

def test_keycloak_token_get_with_existing_token(keycloak_token):
    # Set the token to a non-None value to test the branch where _token is already set
    keycloak_token._token = "existing_token"
    assert keycloak_token.get() == "existing_token"

def test_keycloak_token_get_without_existing_token(keycloak_token, mocked_open_url):
    # _token is None, so the branch where _token is not set will be tested
    assert keycloak_token.get() == "test_access_token"
    # Ensure that the token is now set to the value from the mocked response
    assert keycloak_token._token == "test_access_token"
