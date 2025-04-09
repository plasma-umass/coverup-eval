# file: lib/ansible/galaxy/token.py:62-64
# asked: {"lines": [62, 63, 64], "branches": []}
# gained: {"lines": [62, 63, 64], "branches": []}

import pytest
from ansible.galaxy.token import KeycloakToken

def test_form_payload():
    token = KeycloakToken(client_id="test_client", access_token="test_token")
    payload = token._form_payload()
    assert payload == "grant_type=refresh_token&client_id=test_client&refresh_token=test_token"
