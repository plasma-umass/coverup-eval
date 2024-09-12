# file: tornado/auth.py:1176-1187
# asked: {"lines": [1180, 1181, 1182, 1185, 1186, 1187], "branches": []}
# gained: {"lines": [1180, 1181, 1182, 1185, 1186, 1187], "branches": []}

import pytest
from tornado.auth import _oauth_parse_response
from tornado import escape
import urllib.parse

def test_oauth_parse_response(monkeypatch):
    # Mock the escape.native_str function to return a controlled string
    def mock_native_str(body):
        return body.decode('utf-8')
    
    monkeypatch.setattr(escape, 'native_str', mock_native_str)
    
    # Test case with only required parameters
    body = b'oauth_token=test_token&oauth_token_secret=test_secret'
    expected = {'key': 'test_token', 'secret': 'test_secret'}
    result = _oauth_parse_response(body)
    assert result == expected
    
    # Test case with additional parameters
    body = b'oauth_token=test_token&oauth_token_secret=test_secret&extra_param=extra_value'
    expected = {'key': 'test_token', 'secret': 'test_secret', 'extra_param': 'extra_value'}
    result = _oauth_parse_response(body)
    assert result == expected
    
    # Test case with no parameters (should raise KeyError)
    body = b''
    with pytest.raises(KeyError):
        _oauth_parse_response(body)
    
    # Test case with missing required parameters (should raise KeyError)
    body = b'oauth_token=test_token'
    with pytest.raises(KeyError):
        _oauth_parse_response(body)
    
    body = b'oauth_token_secret=test_secret'
    with pytest.raises(KeyError):
        _oauth_parse_response(body)
