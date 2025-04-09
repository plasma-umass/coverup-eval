# file: lib/ansible/galaxy/token.py:53-60
# asked: {"lines": [53, 54, 55, 56, 57, 58, 59, 60], "branches": [[59, 0], [59, 60]]}
# gained: {"lines": [53, 54, 55, 56, 57, 58, 59, 60], "branches": [[59, 0], [59, 60]]}

import pytest
from ansible.galaxy.token import KeycloakToken

def test_keycloak_token_initialization_with_client_id():
    token = KeycloakToken(access_token="dummy_token", auth_url="http://example.com", validate_certs=False, client_id="test_client")
    assert token.access_token == "dummy_token"
    assert token.auth_url == "http://example.com"
    assert token.validate_certs is False
    assert token.client_id == "test_client"

def test_keycloak_token_initialization_without_client_id():
    token = KeycloakToken(access_token="dummy_token", auth_url="http://example.com", validate_certs=False)
    assert token.access_token == "dummy_token"
    assert token.auth_url == "http://example.com"
    assert token.validate_certs is False
    assert token.client_id == "cloud-services"
