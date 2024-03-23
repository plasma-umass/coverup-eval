# file lib/ansible/galaxy/token.py:45-52
# lines [45, 46, 51]
# branches []

import pytest
from ansible.galaxy.token import KeycloakToken

def test_keycloak_token_type():
    # Test to ensure the token_type attribute is 'Bearer'
    token = KeycloakToken()
    assert token.token_type == 'Bearer'
