# file tornado/auth.py:416-438
# lines [422, 423, 424, 425, 426, 427, 429, 430, 431, 432, 433, 434, 435, 436, 438]
# branches ['431->432', '431->434', '434->435', '434->438']

import pytest
from unittest import mock
from tornado.web import RequestHandler
from tornado.httpclient import HTTPResponse, HTTPRequest
from tornado.auth import OAuthMixin
from tornado import escape
import base64
import urllib.parse

class MockHandler(RequestHandler, OAuthMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._cookies = {}
        self.redirect_url = None
        self.finished = False

    def set_cookie(self, name, value):
        self._cookies[name] = value

    def finish(self, chunk=None):
        self.finished = True

    def redirect(self, url, permanent=False, status=None):
        self.redirect_url = url

    @property
    def cookies(self):
        return self._cookies

@pytest.fixture
def mock_handler():
    return MockHandler(mock.MagicMock(), mock.MagicMock())

def test_on_request_token_oob(mock_handler):
    response = mock.MagicMock(spec=HTTPResponse)
    response.body = b'oauth_token=key&oauth_token_secret=secret'
    authorize_url = "http://example.com/authorize"
    callback_uri = "oob"

    mock_handler._on_request_token(authorize_url, callback_uri, response)

    assert mock_handler.cookies["_oauth_request_token"] == (
        base64.b64encode(b"key") + b"|" + base64.b64encode(b"secret")
    )
    assert mock_handler.finished
    assert mock_handler.redirect_url is None

def test_on_request_token_with_callback(mock_handler):
    response = mock.MagicMock(spec=HTTPResponse)
    response.body = b'oauth_token=key&oauth_token_secret=secret'
    authorize_url = "http://example.com/authorize"
    callback_uri = "http://example.com/callback"

    mock_handler.request = mock.MagicMock()
    mock_handler.request.full_url = mock.MagicMock(return_value="http://example.com/request")

    mock_handler._on_request_token(authorize_url, callback_uri, response)

    assert mock_handler.cookies["_oauth_request_token"] == (
        base64.b64encode(b"key") + b"|" + base64.b64encode(b"secret")
    )
    assert not mock_handler.finished
    assert mock_handler.redirect_url == (
        authorize_url + "?oauth_token=key&oauth_callback=http%3A%2F%2Fexample.com%2Fcallback"
    )

def test_on_request_token_no_callback(mock_handler):
    response = mock.MagicMock(spec=HTTPResponse)
    response.body = b'oauth_token=key&oauth_token_secret=secret'
    authorize_url = "http://example.com/authorize"
    callback_uri = None

    mock_handler._on_request_token(authorize_url, callback_uri, response)

    assert mock_handler.cookies["_oauth_request_token"] == (
        base64.b64encode(b"key") + b"|" + base64.b64encode(b"secret")
    )
    assert not mock_handler.finished
    assert mock_handler.redirect_url == authorize_url + "?oauth_token=key"
