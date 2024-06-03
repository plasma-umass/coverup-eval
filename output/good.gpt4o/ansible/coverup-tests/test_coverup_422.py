# file lib/ansible/galaxy/token.py:53-60
# lines [53, 54, 55, 56, 57, 58, 59, 60]
# branches ['59->exit', '59->60']

import pytest
from ansible.galaxy.token import KeycloakToken

def test_keycloak_token_initialization():
    # Test with all parameters provided
    token = KeycloakToken(access_token="test_token", auth_url="http://example.com", validate_certs=False, client_id="test_client")
    assert token.access_token == "test_token"
    assert token.auth_url == "http://example.com"
    assert token.validate_certs is False
    assert token.client_id == "test_client"
    
    # Test with client_id as None
    token = KeycloakToken(access_token="test_token", auth_url="http://example.com", validate_certs=True, client_id=None)
    assert token.client_id == "cloud-services"
    
    # Test with default parameters
    token = KeycloakToken()
    assert token.access_token is None
    assert token.auth_url is None
    assert token.validate_certs is True
    assert token.client_id == "cloud-services"
