# file: tornado/auth.py:1039-1099
# asked: {"lines": [1039, 1042, 1043, 1096, 1097, 1098], "branches": []}
# gained: {"lines": [1039, 1042, 1043], "branches": []}

import pytest
from tornado.auth import FacebookGraphMixin
from tornado.httpclient import AsyncHTTPClient
from unittest.mock import patch, MagicMock

class TestFacebookGraphMixin(FacebookGraphMixin):
    _FACEBOOK_BASE_URL = "https://graph.facebook.com"

@pytest.mark.asyncio
async def test_facebook_request_get(monkeypatch):
    async def mock_oauth2_request(url, access_token=None, post_args=None, **args):
        assert url == "https://graph.facebook.com/me"
        assert access_token == "dummy_access_token"
        assert post_args is None
        assert args == {}
        return {"id": "12345"}

    monkeypatch.setattr(TestFacebookGraphMixin, "oauth2_request", mock_oauth2_request)

    mixin = TestFacebookGraphMixin()
    response = await mixin.facebook_request("/me", access_token="dummy_access_token")
    assert response == {"id": "12345"}

@pytest.mark.asyncio
async def test_facebook_request_post(monkeypatch):
    async def mock_oauth2_request(url, access_token=None, post_args=None, **args):
        assert url == "https://graph.facebook.com/me/feed"
        assert access_token == "dummy_access_token"
        assert post_args == {"message": "Hello World"}
        assert args == {}
        return {"id": "67890"}

    monkeypatch.setattr(TestFacebookGraphMixin, "oauth2_request", mock_oauth2_request)

    mixin = TestFacebookGraphMixin()
    response = await mixin.facebook_request("/me/feed", access_token="dummy_access_token", post_args={"message": "Hello World"})
    assert response == {"id": "67890"}
