# file tornado/auth.py:88-114
# lines [88, 90, 91, 109, 110, 111, 112, 113, 114]
# branches []

import pytest
from unittest.mock import Mock, patch
from tornado.web import RequestHandler, Application
from tornado.auth import OpenIdMixin
import urllib.parse

class MockRequestHandler(RequestHandler, OpenIdMixin):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self._OPENID_ENDPOINT = "http://example.com/openid"

    def _openid_args(self, callback_uri, ax_attrs):
        return {
            "openid.mode": "checkid_setup",
            "openid.return_to": callback_uri,
            "openid.ax_attrs": ax_attrs,
        }

@pytest.fixture
def mock_request_handler(mocker):
    application = Application()
    request = Mock()
    request.uri = "http://example.com/callback"
    handler = MockRequestHandler(application, request)
    return handler

def test_authenticate_redirect(mock_request_handler, mocker):
    mocker.patch.object(mock_request_handler, 'redirect')
    callback_uri = "http://example.com/callback"
    ax_attrs = ["name", "email", "language", "username"]

    mock_request_handler.authenticate_redirect(callback_uri, ax_attrs)

    expected_args = mock_request_handler._openid_args(callback_uri, ax_attrs)
    expected_url = mock_request_handler._OPENID_ENDPOINT + "?" + urllib.parse.urlencode(expected_args)
    mock_request_handler.redirect.assert_called_once_with(expected_url)

    # Test with default callback_uri
    mock_request_handler.authenticate_redirect(None, ax_attrs)
    expected_args = mock_request_handler._openid_args(mock_request_handler.request.uri, ax_attrs)
    expected_url = mock_request_handler._OPENID_ENDPOINT + "?" + urllib.parse.urlencode(expected_args)
    mock_request_handler.redirect.assert_called_with(expected_url)
