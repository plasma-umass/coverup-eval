# file: tornado/auth.py:88-114
# asked: {"lines": [88, 90, 91, 109, 110, 111, 112, 113, 114], "branches": []}
# gained: {"lines": [88, 90, 91, 109, 110, 111, 112, 113, 114], "branches": []}

import pytest
from tornado.web import RequestHandler
from tornado.auth import OpenIdMixin
from unittest.mock import MagicMock, patch
import urllib

class MockRequestHandler(RequestHandler, OpenIdMixin):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self._OPENID_ENDPOINT = "http://example.com/openid"

    def _openid_args(self, callback_uri, ax_attrs):
        return {
            "openid.return_to": callback_uri,
            "openid.ax_attrs": ",".join(ax_attrs),
        }

@pytest.fixture
def mock_handler():
    application = MagicMock()
    request = MagicMock()
    request.uri = "http://example.com/callback"
    return MockRequestHandler(application, request)

def test_authenticate_redirect_default(mock_handler, monkeypatch):
    with patch.object(mock_handler, 'redirect') as mock_redirect:
        mock_handler.authenticate_redirect()
        mock_redirect.assert_called_once()
        args = mock_handler._openid_args(mock_handler.request.uri, ["name", "email", "language", "username"])
        expected_url = mock_handler._OPENID_ENDPOINT + "?" + urllib.parse.urlencode(args)
        assert mock_redirect.call_args[0][0] == expected_url

def test_authenticate_redirect_custom_callback(mock_handler, monkeypatch):
    custom_callback = "http://example.com/custom_callback"
    with patch.object(mock_handler, 'redirect') as mock_redirect:
        mock_handler.authenticate_redirect(callback_uri=custom_callback)
        mock_redirect.assert_called_once()
        args = mock_handler._openid_args(custom_callback, ["name", "email", "language", "username"])
        expected_url = mock_handler._OPENID_ENDPOINT + "?" + urllib.parse.urlencode(args)
        assert mock_redirect.call_args[0][0] == expected_url

def test_authenticate_redirect_custom_ax_attrs(mock_handler, monkeypatch):
    custom_ax_attrs = ["nickname", "dob"]
    with patch.object(mock_handler, 'redirect') as mock_redirect:
        mock_handler.authenticate_redirect(ax_attrs=custom_ax_attrs)
        mock_redirect.assert_called_once()
        args = mock_handler._openid_args(mock_handler.request.uri, custom_ax_attrs)
        expected_url = mock_handler._OPENID_ENDPOINT + "?" + urllib.parse.urlencode(args)
        assert mock_redirect.call_args[0][0] == expected_url
