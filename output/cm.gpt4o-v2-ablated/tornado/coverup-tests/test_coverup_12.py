# file: tornado/auth.py:339-383
# asked: {"lines": [339, 340, 357, 358, 359, 360, 361, 362, 363, 364, 365, 367, 368, 369, 370, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383], "branches": [[361, 362], [361, 363], [367, 368], [367, 369], [372, 373], [372, 374], [374, 375], [374, 376], [380, 381], [380, 382]]}
# gained: {"lines": [339, 340], "branches": []}

import pytest
from tornado.web import RequestHandler
from tornado import httpclient, escape
from tornado.auth import AuthError
from unittest.mock import AsyncMock, MagicMock, patch
import base64

class MockHandler(RequestHandler):
    def get_argument(self, name, default=None):
        if name == "oauth_token":
            return "mock_oauth_token"
        elif name == "oauth_verifier":
            return "mock_oauth_verifier"
        return default

    def get_cookie(self, name):
        if name == "_oauth_request_token":
            return base64.b64encode(b"mock_oauth_token").decode() + "|" + base64.b64encode(b"mock_secret").decode()
        return None

    def clear_cookie(self, name):
        pass

    def get_auth_http_client(self):
        return AsyncMock()

    async def _oauth_access_token_url(self, token):
        return "http://mock_oauth_access_token_url"

    async def _oauth_get_user_future(self, access_token):
        return {"name": "mock_user"}

def _oauth_parse_response(body):
    return {"access_token": "mock_access_token"}

class TestOAuthMixin:
    @pytest.mark.asyncio
    async def test_get_authenticated_user_success(self, monkeypatch):
        handler = MockHandler()
        mixin = OAuthMixin()
        mixin.__dict__.update(handler.__dict__)

        mock_http_client = AsyncMock()
        mock_response = MagicMock()
        mock_response.body = b"access_token=mock_access_token"
        mock_http_client.fetch.return_value = mock_response

        monkeypatch.setattr(mixin, 'get_auth_http_client', lambda: mock_http_client)
        monkeypatch.setattr(mixin, '_oauth_access_token_url', AsyncMock(return_value="http://mock_oauth_access_token_url"))
        monkeypatch.setattr(mixin, '_oauth_get_user_future', AsyncMock(return_value={"name": "mock_user"}))

        user = await mixin.get_authenticated_user()

        assert user["access_token"] == {"access_token": "mock_access_token"}
        assert user["name"] == "mock_user"

    @pytest.mark.asyncio
    async def test_get_authenticated_user_missing_cookie(self):
        handler = MockHandler()
        mixin = OAuthMixin()
        mixin.__dict__.update(handler.__dict__)

        handler.get_cookie = lambda name: None

        with pytest.raises(AuthError, match="Missing OAuth request token cookie"):
            await mixin.get_authenticated_user()

    @pytest.mark.asyncio
    async def test_get_authenticated_user_token_mismatch(self):
        handler = MockHandler()
        mixin = OAuthMixin()
        mixin.__dict__.update(handler.__dict__)

        handler.get_argument = lambda name, default=None: "different_oauth_token"

        with pytest.raises(AuthError, match="Request token does not match cookie"):
            await mixin.get_authenticated_user()

    @pytest.mark.asyncio
    async def test_get_authenticated_user_error_getting_user(self, monkeypatch):
        handler = MockHandler()
        mixin = OAuthMixin()
        mixin.__dict__.update(handler.__dict__)

        mock_http_client = AsyncMock()
        mock_response = MagicMock()
        mock_response.body = b"access_token=mock_access_token"
        mock_http_client.fetch.return_value = mock_response

        monkeypatch.setattr(mixin, 'get_auth_http_client', lambda: mock_http_client)
        monkeypatch.setattr(mixin, '_oauth_access_token_url', AsyncMock(return_value="http://mock_oauth_access_token_url"))
        monkeypatch.setattr(mixin, '_oauth_get_user_future', AsyncMock(return_value=None))

        with pytest.raises(AuthError, match="Error getting user"):
            await mixin.get_authenticated_user()
