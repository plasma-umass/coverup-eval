# file: tornado/auth.py:553-586
# asked: {"lines": [575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586], "branches": [[577, 578], [577, 579], [579, 580], [579, 581], [581, 582], [581, 583], [583, 584], [583, 585]]}
# gained: {"lines": [575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586], "branches": [[577, 578], [577, 579], [579, 580], [579, 581], [581, 582], [581, 583], [583, 584], [583, 585]]}

import pytest
from tornado.web import RequestHandler
from tornado.httputil import url_concat
from typing import Dict, Any, List, Optional
from unittest.mock import MagicMock, patch
from tornado.auth import OAuth2Mixin

class TestHandler(RequestHandler, OAuth2Mixin):
    _OAUTH_AUTHORIZE_URL = "http://example.com/authorize"

@pytest.fixture
def handler():
    application = MagicMock()
    request = MagicMock()
    return TestHandler(application, request)

def test_authorize_redirect_all_params(handler, monkeypatch):
    redirect_uri = "http://example.com/redirect"
    client_id = "test_client_id"
    client_secret = "test_client_secret"
    extra_params = {"state": "xyz"}
    scope = ["email", "profile"]
    response_type = "token"

    def mock_redirect(url):
        assert url.startswith("http://example.com/authorize")
        assert "response_type=token" in url
        assert "redirect_uri=http%3A%2F%2Fexample.com%2Fredirect" in url
        assert "client_id=test_client_id" in url
        assert "state=xyz" in url
        assert "scope=email+profile" in url

    monkeypatch.setattr(handler, "redirect", mock_redirect)
    handler.authorize_redirect(redirect_uri, client_id, client_secret, extra_params, scope, response_type)

def test_authorize_redirect_no_optional_params(handler, monkeypatch):
    def mock_redirect(url):
        assert url.startswith("http://example.com/authorize")
        assert "response_type=code" in url
        assert "redirect_uri" not in url
        assert "client_id" not in url
        assert "state" not in url
        assert "scope" not in url

    monkeypatch.setattr(handler, "redirect", mock_redirect)
    handler.authorize_redirect()

def test_authorize_redirect_some_params(handler, monkeypatch):
    redirect_uri = "http://example.com/redirect"
    client_id = "test_client_id"

    def mock_redirect(url):
        assert url.startswith("http://example.com/authorize")
        assert "response_type=code" in url
        assert "redirect_uri=http%3A%2F%2Fexample.com%2Fredirect" in url
        assert "client_id=test_client_id" in url
        assert "state" not in url
        assert "scope" not in url

    monkeypatch.setattr(handler, "redirect", mock_redirect)
    handler.authorize_redirect(redirect_uri, client_id)
