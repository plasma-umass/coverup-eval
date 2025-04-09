# file: tornado/auth.py:553-586
# asked: {"lines": [553, 555, 556, 557, 558, 559, 560, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586], "branches": [[577, 578], [577, 579], [579, 580], [579, 581], [581, 582], [581, 583], [583, 584], [583, 585]]}
# gained: {"lines": [553, 555, 556, 557, 558, 559, 560, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586], "branches": [[577, 578], [577, 579], [579, 580], [579, 581], [581, 582], [581, 583], [583, 584], [583, 585]]}

import pytest
from unittest.mock import MagicMock
from tornado.web import RequestHandler, Application
from tornado.auth import OAuth2Mixin
from tornado.httputil import HTTPServerRequest

class TestOAuth2Mixin(OAuth2Mixin, RequestHandler):
    _OAUTH_AUTHORIZE_URL = "http://example.com/authorize"

@pytest.fixture
def handler(monkeypatch):
    application = Application()
    request = HTTPServerRequest(uri="/")
    request.connection = MagicMock()
    handler = TestOAuth2Mixin(application, request)
    return handler

def test_authorize_redirect(handler, monkeypatch):
    mock_redirect = MagicMock()
    monkeypatch.setattr(handler, "redirect", mock_redirect)

    handler.authorize_redirect(
        redirect_uri="http://example.com/redirect",
        client_id="test_client_id",
        client_secret="test_client_secret",
        extra_params={"extra_param": "extra_value"},
        scope=["scope1", "scope2"],
        response_type="token"
    )

    expected_url = "http://example.com/authorize?response_type=token&redirect_uri=http%3A%2F%2Fexample.com%2Fredirect&client_id=test_client_id&extra_param=extra_value&scope=scope1+scope2"
    mock_redirect.assert_called_once_with(expected_url)

def test_authorize_redirect_no_optional_params(handler, monkeypatch):
    mock_redirect = MagicMock()
    monkeypatch.setattr(handler, "redirect", mock_redirect)

    handler.authorize_redirect()

    expected_url = "http://example.com/authorize?response_type=code"
    mock_redirect.assert_called_once_with(expected_url)
