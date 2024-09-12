# file: tornado/auth.py:88-114
# asked: {"lines": [88, 90, 91, 109, 110, 111, 112, 113, 114], "branches": []}
# gained: {"lines": [88, 90, 91, 109, 110, 111, 112, 113, 114], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from tornado.web import RequestHandler
from tornado.auth import OpenIdMixin
import urllib.parse

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
def mock_request_handler():
    application = MagicMock()
    request = MagicMock()
    request.uri = "http://example.com/callback"
    return MockRequestHandler(application, request)

def test_authenticate_redirect_default(mock_request_handler, monkeypatch):
    mock_redirect = MagicMock()
    monkeypatch.setattr(mock_request_handler, 'redirect', mock_redirect)

    mock_request_handler.authenticate_redirect()

    expected_args = {
        "openid.return_to": "http://example.com/callback",
        "openid.ax_attrs": "name,email,language,username",
    }
    expected_url = "http://example.com/openid?" + urllib.parse.urlencode(expected_args)
    mock_redirect.assert_called_once_with(expected_url)

def test_authenticate_redirect_custom_callback(mock_request_handler, monkeypatch):
    mock_redirect = MagicMock()
    monkeypatch.setattr(mock_request_handler, 'redirect', mock_redirect)

    custom_callback = "http://example.com/custom_callback"
    mock_request_handler.authenticate_redirect(callback_uri=custom_callback)

    expected_args = {
        "openid.return_to": custom_callback,
        "openid.ax_attrs": "name,email,language,username",
    }
    expected_url = "http://example.com/openid?" + urllib.parse.urlencode(expected_args)
    mock_redirect.assert_called_once_with(expected_url)

def test_authenticate_redirect_custom_ax_attrs(mock_request_handler, monkeypatch):
    mock_redirect = MagicMock()
    monkeypatch.setattr(mock_request_handler, 'redirect', mock_redirect)

    custom_ax_attrs = ["nickname", "dob"]
    mock_request_handler.authenticate_redirect(ax_attrs=custom_ax_attrs)

    expected_args = {
        "openid.return_to": "http://example.com/callback",
        "openid.ax_attrs": "nickname,dob",
    }
    expected_url = "http://example.com/openid?" + urllib.parse.urlencode(expected_args)
    mock_redirect.assert_called_once_with(expected_url)
