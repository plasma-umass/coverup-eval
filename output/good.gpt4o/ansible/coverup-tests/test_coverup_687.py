# file lib/ansible/galaxy/token.py:45-52
# lines [45, 46, 51]
# branches []

import pytest
from ansible.galaxy.token import KeycloakToken

def test_keycloak_token_initialization():
    # Create an instance of KeycloakToken
    token = KeycloakToken()
    
    # Assert that the token_type is 'Bearer'
    assert token.token_type == 'Bearer'
