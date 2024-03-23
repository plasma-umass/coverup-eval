# file lib/ansible/galaxy/token.py:161-187
# lines [161, 162, 164, 165, 166, 167, 169, 170, 171, 172, 173, 174, 176, 177, 178, 180, 182, 184, 185, 186, 187]
# branches ['177->178', '177->180']

import base64
import pytest
from ansible.galaxy.token import BasicAuthToken

# Mocking the to_text and to_bytes functions as they are not provided in the snippet
def to_text(value, errors='strict', nonstring='simplerepr'):
    if isinstance(value, bytes):
        return value.decode('utf-8', errors)
    elif isinstance(value, str):
        return value
    else:
        return str(value) if nonstring == 'simplerepr' else value

def to_bytes(value, encoding='utf-8', errors='strict'):
    if isinstance(value, bytes):
        return value
    elif isinstance(value, str):
        return value.encode(encoding, errors)
    else:
        raise ValueError("Expected bytes or str, got %r" % (value,))

# Patching the to_text and to_bytes functions in the BasicAuthToken class
@pytest.fixture(autouse=True)
def mock_text_bytes(mocker):
    mocker.patch('ansible.galaxy.token.to_text', side_effect=to_text)
    mocker.patch('ansible.galaxy.token.to_bytes', side_effect=to_bytes)

def test_basic_auth_token():
    username = 'testuser'
    password = 'testpass'
    token = BasicAuthToken(username, password)

    # Test the _encode_token static method
    encoded_creds = token._encode_token(username, password)
    expected_b64 = base64.b64encode(f"{username}:{password}".encode('utf-8')).decode('utf-8')
    assert encoded_creds == expected_b64, "The encoded token does not match the expected base64 value"

    # Test the get method
    assert token.get() == expected_b64, "The token retrieved by get() does not match the expected value"

    # Test the headers method
    headers = token.headers()
    assert 'Authorization' in headers, "Authorization header is missing"
    assert headers['Authorization'] == f'Basic {expected_b64}', "Authorization header does not have the correct format"

    # Test that the token is cached
    token._token = 'cached_token'
    assert token.get() == 'cached_token', "The token should be retrieved from the cache"
