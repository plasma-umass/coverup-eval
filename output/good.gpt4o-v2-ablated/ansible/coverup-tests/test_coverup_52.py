# file: lib/ansible/galaxy/token.py:161-187
# asked: {"lines": [161, 162, 164, 165, 166, 167, 169, 170, 171, 172, 173, 174, 176, 177, 178, 180, 182, 184, 185, 186, 187], "branches": [[177, 178], [177, 180]]}
# gained: {"lines": [161, 162, 164, 165, 166, 167, 169, 170, 171, 172, 173, 174, 176, 177, 178, 180, 182, 184, 185, 186, 187], "branches": [[177, 178], [177, 180]]}

import pytest
import base64
from ansible.module_utils._text import to_text, to_bytes

# Assuming the BasicAuthToken class is defined in ansible/galaxy/token.py
from ansible.galaxy.token import BasicAuthToken

@pytest.fixture
def basic_auth_token():
    return BasicAuthToken(username="user", password="pass")

def test_encode_token():
    username = "user"
    password = "pass"
    expected_token = base64.b64encode(to_bytes(f"{username}:{password}", encoding='utf-8', errors='surrogate_or_strict')).decode('utf-8')
    assert BasicAuthToken._encode_token(username, password) == expected_token

def test_get_token(basic_auth_token):
    token = basic_auth_token.get()
    expected_token = base64.b64encode(to_bytes("user:pass", encoding='utf-8', errors='surrogate_or_strict')).decode('utf-8')
    assert token == expected_token

def test_get_token_cached(basic_auth_token, mocker):
    mocker.patch.object(BasicAuthToken, '_encode_token', return_value="cached_token")
    token = basic_auth_token.get()
    assert token == "cached_token"
    # Call get again to ensure the cached token is used
    token = basic_auth_token.get()
    assert token == "cached_token"
    BasicAuthToken._encode_token.assert_called_once_with("user", "pass")

def test_headers(basic_auth_token):
    headers = basic_auth_token.headers()
    expected_token = base64.b64encode(to_bytes("user:pass", encoding='utf-8', errors='surrogate_or_strict')).decode('utf-8')
    assert headers == {'Authorization': f'Basic {expected_token}'}

def test_headers_with_cached_token(basic_auth_token, mocker):
    mocker.patch.object(BasicAuthToken, '_encode_token', return_value="cached_token")
    basic_auth_token.get()  # This will cache the token
    headers = basic_auth_token.headers()
    assert headers == {'Authorization': 'Basic cached_token'}
