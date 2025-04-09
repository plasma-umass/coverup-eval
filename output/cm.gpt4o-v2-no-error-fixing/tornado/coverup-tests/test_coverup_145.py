# file: tornado/auth.py:1102-1132
# asked: {"lines": [1113, 1114, 1115, 1117, 1118, 1119, 1120, 1121, 1122, 1125, 1127, 1128, 1129, 1131, 1132], "branches": []}
# gained: {"lines": [1113, 1114, 1115, 1117, 1118, 1119, 1120, 1121, 1122, 1125, 1127, 1128, 1129, 1131, 1132], "branches": []}

import pytest
from tornado.auth import _oauth_signature
from tornado.escape import utf8
import urllib.parse
import binascii
import hashlib
import hmac

def _oauth_escape(val):
    if isinstance(val, str):
        val = val.encode('utf-8')
    return urllib.parse.quote(val, safe='~')

def test_oauth_signature_full_coverage():
    consumer_token = {"key": "test_consumer_key", "secret": "test_consumer_secret"}
    token = {"key": "test_token_key", "secret": "test_token_secret"}
    method = "POST"
    url = "https://api.example.com/resource"
    parameters = {"param1": "value1", "param2": "value2"}

    signature = _oauth_signature(consumer_token, method, url, parameters, token)
    
    # Verify the signature is correctly generated
    assert isinstance(signature, bytes)
    
    # Manually calculate the expected signature to compare
    parts = urllib.parse.urlparse(url)
    scheme, netloc, path = parts[:3]
    normalized_url = scheme.lower() + "://" + netloc.lower() + path

    base_elems = []
    base_elems.append(method.upper())
    base_elems.append(normalized_url)
    base_elems.append("&".join("%s=%s" % (k, _oauth_escape(str(v))) for k, v in sorted(parameters.items())))
    base_string = "&".join(_oauth_escape(e) for e in base_elems)

    key_elems = [utf8(consumer_token["secret"])]
    key_elems.append(utf8(token["secret"] if token else ""))
    key = b"&".join(key_elems)

    hash = hmac.new(key, utf8(base_string), hashlib.sha1)
    expected_signature = binascii.b2a_base64(hash.digest())[:-1]

    assert signature == expected_signature

