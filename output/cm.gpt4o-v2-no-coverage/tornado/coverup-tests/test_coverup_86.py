# file: tornado/auth.py:1176-1187
# asked: {"lines": [1176, 1180, 1181, 1182, 1185, 1186, 1187], "branches": []}
# gained: {"lines": [1176, 1180, 1181, 1182, 1185, 1186, 1187], "branches": []}

import pytest
from tornado.auth import _oauth_parse_response

def test_oauth_parse_response():
    body = b'oauth_token=test_token&oauth_token_secret=test_secret&extra_param=extra_value'
    expected_result = {
        'key': 'test_token',
        'secret': 'test_secret',
        'extra_param': 'extra_value'
    }
    
    result = _oauth_parse_response(body)
    
    assert result == expected_result

def test_oauth_parse_response_no_extra_params():
    body = b'oauth_token=test_token&oauth_token_secret=test_secret'
    expected_result = {
        'key': 'test_token',
        'secret': 'test_secret'
    }
    
    result = _oauth_parse_response(body)
    
    assert result == expected_result

def test_oauth_parse_response_missing_token():
    body = b'oauth_token_secret=test_secret'
    with pytest.raises(KeyError):
        _oauth_parse_response(body)

def test_oauth_parse_response_missing_secret():
    body = b'oauth_token=test_token'
    with pytest.raises(KeyError):
        _oauth_parse_response(body)
