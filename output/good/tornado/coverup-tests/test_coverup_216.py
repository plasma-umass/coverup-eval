# file tornado/auth.py:1102-1132
# lines [1113, 1114, 1115, 1117, 1118, 1119, 1120, 1121, 1122, 1125, 1127, 1128, 1129, 1131, 1132]
# branches []

import pytest
import hmac
import hashlib
import binascii
from tornado.auth import _oauth_signature
from tornado import escape

@pytest.fixture
def consumer_token():
    return {'key': 'consumer_key', 'secret': 'consumer_secret'}

@pytest.fixture
def token():
    return {'key': 'token_key', 'secret': 'token_secret'}

@pytest.fixture
def parameters():
    return {'param1': 'value1', 'param2': 'value2'}

def test_oauth_signature(consumer_token, token, parameters):
    method = 'GET'
    url = 'http://example.com/api'
    signature = _oauth_signature(consumer_token, method, url, parameters, token)

    # Create the base string for signature
    base_elems = [
        method.upper(),
        'http://example.com/api',
        '&'.join('%s=%s' % (k, escape.url_escape(str(v))) for k, v in sorted(parameters.items()))
    ]
    base_string = '&'.join(escape.url_escape(e) for e in base_elems)

    # Create the signing key
    key_elems = [escape.utf8(consumer_token['secret']), escape.utf8(token['secret'])]
    key = b'&'.join(key_elems)

    # Calculate the HMAC-SHA1 signature
    hash = hmac.new(key, escape.utf8(base_string), hashlib.sha1)
    expected_signature = binascii.b2a_base64(hash.digest())[:-1]

    assert signature == expected_signature, "The OAuth signature does not match the expected value."

