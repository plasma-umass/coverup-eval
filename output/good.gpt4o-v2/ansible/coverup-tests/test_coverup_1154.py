# file: lib/ansible/galaxy/token.py:161-187
# asked: {"lines": [165, 166, 167, 171, 172, 173, 174, 177, 178, 180, 182, 185, 186, 187], "branches": [[177, 178], [177, 180]]}
# gained: {"lines": [165, 166, 167, 171, 172, 173, 174, 177, 178, 180, 182, 185, 186, 187], "branches": [[177, 178], [177, 180]]}

import pytest
from ansible.galaxy.token import BasicAuthToken

def test_basic_auth_token_init():
    token = BasicAuthToken("user", "pass")
    assert token.username == "user"
    assert token.password == "pass"
    assert token._token is None

def test_basic_auth_token_encode_token():
    encoded = BasicAuthToken._encode_token("user", "pass")
    assert encoded == "dXNlcjpwYXNz"

def test_basic_auth_token_get():
    token = BasicAuthToken("user", "pass")
    assert token.get() == "dXNlcjpwYXNz"
    assert token._token == "dXNlcjpwYXNz"

def test_basic_auth_token_get_with_existing_token():
    token = BasicAuthToken("user", "pass")
    token._token = "existing_token"
    assert token.get() == "existing_token"

def test_basic_auth_token_headers():
    token = BasicAuthToken("user", "pass")
    headers = token.headers()
    assert headers["Authorization"] == "Basic dXNlcjpwYXNz"

def test_basic_auth_token_headers_with_existing_token():
    token = BasicAuthToken("user", "pass")
    token._token = "existing_token"
    headers = token.headers()
    assert headers["Authorization"] == "Basic existing_token"
