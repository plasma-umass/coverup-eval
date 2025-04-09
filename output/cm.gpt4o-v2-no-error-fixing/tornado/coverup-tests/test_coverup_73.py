# file: tornado/auth.py:1039-1099
# asked: {"lines": [1039, 1042, 1043, 1096, 1097, 1098], "branches": []}
# gained: {"lines": [1039, 1042, 1043], "branches": []}

import pytest
from tornado.auth import FacebookGraphMixin
from tornado.httpclient import AsyncHTTPClient, HTTPResponse, HTTPRequest
from tornado.escape import json_encode
from unittest.mock import patch, MagicMock

class MockFacebookGraphMixin(FacebookGraphMixin):
    _FACEBOOK_BASE_URL = "https://graph.facebook.com"

@pytest.mark.asyncio
async def test_facebook_request_get(monkeypatch):
    async def mock_fetch(request, **kwargs):
        assert request.url == "https://graph.facebook.com/me"
        return HTTPResponse(request, 200, buffer=json_encode({"id": "12345"}).encode())

    monkeypatch.setattr(AsyncHTTPClient, "fetch", mock_fetch)

    mixin = MockFacebookGraphMixin()
    response = await mixin.facebook_request("/me", access_token="dummy_token")
    assert response == {"id": "12345"}

@pytest.mark.asyncio
async def test_facebook_request_post(monkeypatch):
    async def mock_fetch(request, **kwargs):
        assert request.url == "https://graph.facebook.com/me/feed"
        assert request.method == "POST"
        assert request.body == b"message=Hello+World"
        return HTTPResponse(request, 200, buffer=json_encode({"success": True}).encode())

    monkeypatch.setattr(AsyncHTTPClient, "fetch", mock_fetch)

    mixin = MockFacebookGraphMixin()
    response = await mixin.facebook_request("/me/feed", access_token="dummy_token", post_args={"message": "Hello World"})
    assert response == {"success": True}
