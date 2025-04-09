# file: tornado/auth.py:1176-1187
# asked: {"lines": [1176, 1180, 1181, 1182, 1185, 1186, 1187], "branches": []}
# gained: {"lines": [1176, 1180, 1181, 1182, 1185, 1186, 1187], "branches": []}

import pytest
from tornado.auth import _oauth_parse_response
from tornado.escape import native_str
import urllib.parse

def test_oauth_parse_response(monkeypatch):
    # Mocking the escape.native_str function to return the input as a string
    monkeypatch.setattr('tornado.escape.native_str', lambda x: x.decode('utf-8'))

    # Mock response body
    body = b'oauth_token=test_token&oauth_token_secret=test_secret&extra_param=extra_value'

    # Call the function
    result = _oauth_parse_response(body)

    # Assertions to verify the postconditions
    assert result['key'] == 'test_token'
    assert result['secret'] == 'test_secret'
    assert result['extra_param'] == 'extra_value'
