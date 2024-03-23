# file lib/ansible/galaxy/token.py:53-60
# lines [53, 54, 55, 56, 57, 58, 59, 60]
# branches ['59->exit', '59->60']

import pytest
from ansible.galaxy.token import KeycloakToken

@pytest.fixture
def keycloak_token_cleanup():
    # Setup code if necessary
    yield
    # Cleanup code if necessary

def test_keycloak_token_initialization(keycloak_token_cleanup):
    token = KeycloakToken(access_token='dummy_access_token', auth_url='https://dummy.auth.url', validate_certs=False, client_id='dummy_client_id')
    assert token.access_token == 'dummy_access_token'
    assert token.auth_url == 'https://dummy.auth.url'
    assert token.validate_certs is False
    assert token.client_id == 'dummy_client_id'

    token_default_client_id = KeycloakToken(access_token='dummy_access_token', auth_url='https://dummy.auth.url', validate_certs=True)
    assert token_default_client_id.client_id == 'cloud-services'
