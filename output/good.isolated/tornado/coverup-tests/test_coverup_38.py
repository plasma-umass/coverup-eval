# file tornado/auth.py:416-438
# lines [416, 422, 423, 424, 425, 426, 427, 429, 430, 431, 432, 433, 434, 435, 436, 438]
# branches ['431->432', '431->434', '434->435', '434->438']

import base64
import pytest
from tornado import escape, httpclient
from tornado.auth import OAuthMixin
from unittest.mock import Mock
from urllib.parse import urlencode

# Mocking the RequestHandler to be used in the OAuthMixin
class MockRequestHandler:
    def __init__(self):
        self.cookies = {}
        self.finished = False
        self.redirected = False
        self.redirect_url = None
        self.finish_chunk = None
        self.request = Mock(full_url=Mock(return_value='http://example.com/'))

    def set_cookie(self, name, value):
        self.cookies[name] = value

    def finish(self, chunk=None):
        self.finished = True
        self.finish_chunk = chunk

    def redirect(self, url):
        self.redirected = True
        self.redirect_url = url

# Mocking the _oauth_parse_response function
def mock_oauth_parse_response(response_body):
    return {
        "key": "test_key",
        "secret": "test_secret"
    }

# Test function to cover the missing branches
@pytest.mark.parametrize("callback_uri,expected_finish,expected_redirect", [
    ("oob", True, False),
    ("http://callback.example.com", False, True),
    (None, False, True)
])
def test_on_request_token(callback_uri, expected_finish, expected_redirect, mocker):
    mocker.patch('tornado.auth._oauth_parse_response', side_effect=mock_oauth_parse_response)

    mixin = OAuthMixin()
    handler = MockRequestHandler()
    mixin._on_request_token = OAuthMixin._on_request_token.__get__(handler)
    response = httpclient.HTTPResponse(Mock(), 200, buffer=Mock())

    authorize_url = "http://authorize.example.com"
    mixin._on_request_token(authorize_url, callback_uri, response)

    assert handler.finished == expected_finish
    assert handler.redirected == expected_redirect

    if expected_finish:
        assert handler.finish_chunk.startswith(authorize_url)
        assert "oauth_token=test_key" in handler.finish_chunk

    if expected_redirect:
        assert handler.redirect_url.startswith(authorize_url)
        assert "oauth_token=test_key" in handler.redirect_url

    # Check if the cookie is set correctly
    encoded_key = base64.b64encode(escape.utf8("test_key")).decode()
    encoded_secret = base64.b64encode(escape.utf8("test_secret")).decode()
    expected_cookie = f"{encoded_key}|{encoded_secret}"
    assert handler.cookies["_oauth_request_token"].decode() == expected_cookie
