# file: tornado/auth.py:1135-1167
# asked: {"lines": [1146, 1147, 1148, 1150, 1151, 1152, 1153, 1154, 1155, 1159, 1160, 1161, 1162, 1164, 1166, 1167], "branches": []}
# gained: {"lines": [1146, 1147, 1148, 1150, 1151, 1152, 1153, 1154, 1155, 1159, 1160, 1161, 1162, 1164, 1166, 1167], "branches": []}

import pytest
import urllib.parse
import binascii
import hashlib
import hmac
from tornado.auth import _oauth10a_signature
from tornado.escape import utf8
from tornado.util import unicode_type

def test_oauth10a_signature(monkeypatch):
    def mock_utf8(value):
        if isinstance(value, str):
            return value.encode('utf-8')
        return value

    def mock_oauth_escape(val):
        if isinstance(val, unicode_type):
            val = val.encode('utf-8')
        return urllib.parse.quote(val, safe='~')

    monkeypatch.setattr('tornado.escape.utf8', mock_utf8)
    monkeypatch.setattr('tornado.auth._oauth_escape', mock_oauth_escape)

    consumer_token = {"key": "test_consumer_key", "secret": "test_consumer_secret"}
    token = {"key": "test_token_key", "secret": "test_token_secret"}
    method = "POST"
    url = "https://api.example.com/resource"
    parameters = {"param1": "value1", "param2": "value2"}

    signature = _oauth10a_signature(consumer_token, method, url, parameters, token)
    
    assert isinstance(signature, bytes)
    
    # Calculate the expected signature value manually
    parts = urllib.parse.urlparse(url)
    scheme, netloc, path = parts[:3]
    normalized_url = scheme.lower() + "://" + netloc.lower() + path

    base_elems = []
    base_elems.append(method.upper())
    base_elems.append(normalized_url)
    base_elems.append(
        "&".join(
            "%s=%s" % (k, mock_oauth_escape(str(v))) for k, v in sorted(parameters.items())
        )
    )

    base_string = "&".join(mock_oauth_escape(e) for e in base_elems)
    key_elems = [mock_utf8(urllib.parse.quote(consumer_token["secret"], safe="~"))]
    key_elems.append(
        mock_utf8(urllib.parse.quote(token["secret"], safe="~") if token else "")
    )
    key = b"&".join(key_elems)

    hash = hmac.new(key, mock_utf8(base_string), hashlib.sha1)
    expected_signature_value = binascii.b2a_base64(hash.digest())[:-1]

    assert signature == expected_signature_value

    # Clean up monkeypatch
    monkeypatch.undo()
