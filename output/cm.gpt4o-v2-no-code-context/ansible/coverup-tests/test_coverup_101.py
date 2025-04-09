# file: lib/ansible/galaxy/token.py:161-187
# asked: {"lines": [161, 162, 164, 165, 166, 167, 169, 170, 171, 172, 173, 174, 176, 177, 178, 180, 182, 184, 185, 186, 187], "branches": [[177, 178], [177, 180]]}
# gained: {"lines": [161, 162, 164, 165, 166, 167, 169, 170, 171, 172, 173, 174, 176, 177, 178, 180, 182, 184, 185, 186, 187], "branches": [[177, 178], [177, 180]]}

import pytest
import base64
from ansible.module_utils._text import to_text, to_bytes
from ansible.galaxy.token import BasicAuthToken

@pytest.fixture
def basic_auth_token():
    return BasicAuthToken(username="testuser", password="testpass")

def test_basic_auth_token_init(basic_auth_token):
    assert basic_auth_token.username == "testuser"
    assert basic_auth_token.password == "testpass"
    assert basic_auth_token._token is None

def test_basic_auth_token_encode_token():
    encoded_token = BasicAuthToken._encode_token("testuser", "testpass")
    expected_token = base64.b64encode(to_bytes("testuser:testpass", encoding='utf-8', errors='surrogate_or_strict'))
    assert encoded_token == to_text(expected_token)

def test_basic_auth_token_get(basic_auth_token):
    token = basic_auth_token.get()
    expected_token = base64.b64encode(to_bytes("testuser:testpass", encoding='utf-8', errors='surrogate_or_strict'))
    assert token == to_text(expected_token)
    assert basic_auth_token._token == token

def test_basic_auth_token_get_cached_token(basic_auth_token):
    basic_auth_token._token = "cached_token"
    token = basic_auth_token.get()
    assert token == "cached_token"

def test_basic_auth_token_headers(basic_auth_token):
    headers = basic_auth_token.headers()
    expected_token = base64.b64encode(to_bytes("testuser:testpass", encoding='utf-8', errors='surrogate_or_strict'))
    expected_headers = {
        'Authorization': 'Basic %s' % to_text(expected_token)
    }
    assert headers == expected_headers
