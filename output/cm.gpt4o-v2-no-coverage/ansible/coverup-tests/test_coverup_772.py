# file: lib/ansible/galaxy/token.py:62-64
# asked: {"lines": [62, 63, 64], "branches": []}
# gained: {"lines": [62, 63, 64], "branches": []}

import pytest
from ansible.galaxy.token import KeycloakToken

def test_form_payload():
    token = KeycloakToken(access_token="dummy_access_token", client_id="dummy_client_id")
    expected_payload = "grant_type=refresh_token&client_id=dummy_client_id&refresh_token=dummy_access_token"
    assert token._form_payload() == expected_payload

    token = KeycloakToken(access_token="another_token", client_id=None)
    expected_payload = "grant_type=refresh_token&client_id=cloud-services&refresh_token=another_token"
    assert token._form_payload() == expected_payload
