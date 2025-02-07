# file: tornado/auth.py:416-438
# asked: {"lines": [416, 422, 423, 424, 425, 426, 427, 429, 430, 431, 432, 433, 434, 435, 436, 438], "branches": [[431, 432], [431, 434], [434, 435], [434, 438]]}
# gained: {"lines": [416, 422, 423, 424, 425, 426, 427, 429, 430, 431, 432, 433, 434, 435, 436, 438], "branches": [[431, 432], [431, 434], [434, 435], [434, 438]]}

import pytest
from tornado.web import RequestHandler
from tornado.httpclient import HTTPResponse
from tornado.escape import utf8
from unittest.mock import MagicMock, patch
import base64
import urllib.parse
from tornado.auth import OAuthMixin

class TestOAuthMixin:
    @patch('tornado.web.RequestHandler.set_cookie')
    @patch('tornado.web.RequestHandler.finish')
    @patch('tornado.web.RequestHandler.redirect')
    @patch('tornado.auth._oauth_parse_response')
    def test_on_request_token(self, mock_parse_response, mock_redirect, mock_finish, mock_set_cookie):
        class MockHandler(RequestHandler, OAuthMixin):
            def __init__(self):
                self.request = MagicMock()
                self.request.full_url = MagicMock(return_value="http://example.com/full")

        handler = MockHandler()
        authorize_url = "http://example.com/authorize"
        callback_uri = "http://example.com/callback"
        response = MagicMock(spec=HTTPResponse)
        response.body = b'oauth_token=token&oauth_token_secret=secret'

        mock_parse_response.return_value = {
            'key': 'token',
            'secret': 'secret'
        }

        handler._on_request_token(authorize_url, callback_uri, response)

        mock_set_cookie.assert_called_once_with(
            "_oauth_request_token",
            base64.b64encode(utf8("token")) + b"|" + base64.b64encode(utf8("secret"))
        )

        expected_args = dict(oauth_token='token', oauth_callback='http://example.com/callback')
        mock_redirect.assert_called_once_with(authorize_url + "?" + urllib.parse.urlencode(expected_args))

        # Test the 'oob' callback_uri case
        mock_redirect.reset_mock()
        handler._on_request_token(authorize_url, "oob", response)
        mock_finish.assert_called_once_with(authorize_url + "?" + urllib.parse.urlencode(dict(oauth_token='token')))

        # Test the None callback_uri case
        mock_finish.reset_mock()
        handler._on_request_token(authorize_url, None, response)
        expected_args = dict(oauth_token='token')
        mock_redirect.assert_called_once_with(authorize_url + "?" + urllib.parse.urlencode(expected_args))
