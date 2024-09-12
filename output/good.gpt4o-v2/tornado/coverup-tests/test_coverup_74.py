# file: tornado/auth.py:1176-1187
# asked: {"lines": [1176, 1180, 1181, 1182, 1185, 1186, 1187], "branches": []}
# gained: {"lines": [1176, 1180, 1181, 1182, 1185, 1186, 1187], "branches": []}

import pytest
from tornado.auth import _oauth_parse_response

def test_oauth_parse_response():
    body = b'oauth_token=test_token&oauth_token_secret=test_secret&extra_param=extra_value'
    expected_token = {
        'key': 'test_token',
        'secret': 'test_secret',
        'extra_param': 'extra_value'
    }
    
    token = _oauth_parse_response(body)
    
    assert token == expected_token
