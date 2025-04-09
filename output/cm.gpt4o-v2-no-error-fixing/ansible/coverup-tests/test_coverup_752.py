# file: lib/ansible/galaxy/token.py:161-187
# asked: {"lines": [165, 166, 167, 171, 172, 173, 174, 177, 178, 180, 182, 185, 186, 187], "branches": [[177, 178], [177, 180]]}
# gained: {"lines": [165, 166, 167, 171, 172, 173, 174, 177, 178, 180, 182, 185, 186, 187], "branches": [[177, 178], [177, 180]]}

import pytest
from ansible.galaxy.token import BasicAuthToken

@pytest.fixture
def auth_token():
    return BasicAuthToken("user", "pass")

def test_init(auth_token):
    assert auth_token.username == "user"
    assert auth_token.password == "pass"
    assert auth_token._token is None

def test_encode_token():
    encoded = BasicAuthToken._encode_token("user", "pass")
    assert encoded == "dXNlcjpwYXNz"

def test_get_token(auth_token):
    token = auth_token.get()
    assert token == "dXNlcjpwYXNz"
    assert auth_token._token == token

def test_get_token_cached(auth_token):
    auth_token._token = "cached_token"
    token = auth_token.get()
    assert token == "cached_token"

def test_headers(auth_token):
    headers = auth_token.headers()
    assert headers["Authorization"] == "Basic dXNlcjpwYXNz"
