# file: lib/ansible/galaxy/token.py:53-60
# asked: {"lines": [53, 54, 55, 56, 57, 58, 59, 60], "branches": [[59, 0], [59, 60]]}
# gained: {"lines": [53, 54, 55, 56, 57, 58, 59, 60], "branches": [[59, 0], [59, 60]]}

import pytest
from ansible.galaxy.token import KeycloakToken

def test_keycloaktoken_init_with_client_id():
    token = KeycloakToken(client_id="test-client")
    assert token.client_id == "test-client"

def test_keycloaktoken_init_without_client_id():
    token = KeycloakToken()
    assert token.client_id == "cloud-services"
