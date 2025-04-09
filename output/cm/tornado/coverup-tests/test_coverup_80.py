# file tornado/auth.py:1176-1187
# lines [1176, 1180, 1181, 1182, 1185, 1186, 1187]
# branches []

import pytest
from tornado import escape
from tornado.auth import _oauth_parse_response
from urllib.parse import urlencode

@pytest.fixture
def mock_response(mocker):
    # Mock the response to include oauth_token and oauth_token_secret
    params = {
        'oauth_token': 'test_token',
        'oauth_token_secret': 'test_secret',
        'extra_param': 'extra_value'
    }
    body = urlencode(params).encode('utf-8')
    return body

def test_oauth_parse_response(mock_response):
    # Test the _oauth_parse_response function
    token = _oauth_parse_response(mock_response)
    assert token['key'] == 'test_token'
    assert token['secret'] == 'test_secret'
    assert token['extra_param'] == 'extra_value'
