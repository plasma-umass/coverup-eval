# file lib/ansible/galaxy/token.py:161-187
# lines [161, 162, 164, 165, 166, 167, 169, 170, 171, 172, 173, 174, 176, 177, 178, 180, 182, 184, 185, 186, 187]
# branches ['177->178', '177->180']

import pytest
import base64
from ansible.module_utils._text import to_text, to_bytes
from ansible.galaxy.token import BasicAuthToken

@pytest.fixture
def basic_auth_token():
    return BasicAuthToken(username="testuser", password="testpass")

def test_basic_auth_token_get(basic_auth_token):
    token = basic_auth_token.get()
    expected_token = base64.b64encode(to_bytes("testuser:testpass", encoding='utf-8', errors='surrogate_or_strict')).decode('utf-8')
    assert token == expected_token

def test_basic_auth_token_headers(basic_auth_token):
    headers = basic_auth_token.headers()
    expected_token = base64.b64encode(to_bytes("testuser:testpass", encoding='utf-8', errors='surrogate_or_strict')).decode('utf-8')
    assert headers == {'Authorization': f'Basic {expected_token}'}

def test_basic_auth_token_no_password():
    token_instance = BasicAuthToken(username="testuser")
    token = token_instance.get()
    expected_token = base64.b64encode(to_bytes("testuser:", encoding='utf-8', errors='surrogate_or_strict')).decode('utf-8')
    assert token == expected_token

def test_basic_auth_token_headers_no_password():
    token_instance = BasicAuthToken(username="testuser")
    headers = token_instance.headers()
    expected_token = base64.b64encode(to_bytes("testuser:", encoding='utf-8', errors='surrogate_or_strict')).decode('utf-8')
    assert headers == {'Authorization': f'Basic {expected_token}'}
