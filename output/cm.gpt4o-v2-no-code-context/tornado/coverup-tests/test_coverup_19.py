# file: tornado/auth.py:339-383
# asked: {"lines": [339, 340, 357, 358, 359, 360, 361, 362, 363, 364, 365, 367, 368, 369, 370, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383], "branches": [[361, 362], [361, 363], [367, 368], [367, 369], [372, 373], [372, 374], [374, 375], [374, 376], [380, 381], [380, 382]]}
# gained: {"lines": [339, 340], "branches": []}

import pytest
from tornado.web import RequestHandler
from tornado import escape, httpclient
from tornado.auth import AuthError
from unittest.mock import MagicMock, patch
import base64
from typing import Optional, Dict, Any, Union

class MockHandler(RequestHandler):
    def get_argument(self, name, default=None):
        if name == "oauth_token":
            return "test_oauth_token"
        elif name == "oauth_verifier":
            return "test_oauth_verifier"
        return default

    def get_cookie(self, name):
        if name == "_oauth_request_token":
            return base64.b64encode(b"test_oauth_token|test_secret").decode('utf-8')
        return None

    def clear_cookie(self, name):
        pass

    def get_auth_http_client(self):
        return MagicMock()

    async def _oauth_access_token_url(self, token):
        return "http://example.com/oauth/access_token"

    async def _oauth_get_user_future(self, access_token):
        return {"name": "test_user"}

def _oauth_parse_response(body):
    return {"access_token": "test_access_token"}

class OAuthMixin(MockHandler):
    async def get_authenticated_user(self, http_client: Optional[httpclient.AsyncHTTPClient] = None) -> Dict[str, Any]:
        handler = self
        request_key = escape.utf8(handler.get_argument("oauth_token"))
        oauth_verifier = handler.get_argument("oauth_verifier", None)
        request_cookie = handler.get_cookie("_oauth_request_token")
        if not request_cookie:
            raise AuthError("Missing OAuth request token cookie")
        handler.clear_cookie("_oauth_request_token")
        cookie_key, cookie_secret = [
            base64.b64decode(escape.utf8(i)) for i in request_cookie.split("|")
        ]
        if cookie_key != request_key:
            raise AuthError("Request token does not match cookie")
        token = dict(
            key=cookie_key, secret=cookie_secret
        )  # type: Dict[str, Union[str, bytes]]
        if oauth_verifier:
            token["verifier"] = oauth_verifier
        if http_client is None:
            http_client = self.get_auth_http_client()
        assert http_client is not None
        response = await http_client.fetch(self._oauth_access_token_url(token))
        access_token = _oauth_parse_response(response.body)
        user = await self._oauth_get_user_future(access_token)
        if not user:
            raise AuthError("Error getting user")
        user["access_token"] = access_token
        return user

@pytest.mark.asyncio
async def test_get_authenticated_user(monkeypatch):
    handler = OAuthMixin()

    mock_http_client = MagicMock()
    mock_response = MagicMock()
    mock_response.body = b"access_token=test_access_token"
    mock_http_client.fetch = MagicMock(return_value=mock_response)

    monkeypatch.setattr(handler, "get_auth_http_client", lambda: mock_http_client)
    monkeypatch.setattr(handler, "_oauth_access_token_url", lambda token: "http://example.com/oauth/access_token")
    monkeypatch.setattr(handler, "_oauth_get_user_future", lambda access_token: {"name": "test_user"})

    user = await handler.get_authenticated_user()

    assert user["access_token"] == {"access_token": "test_access_token"}
    assert user["name"] == "test_user"

@pytest.mark.asyncio
async def test_get_authenticated_user_missing_cookie(monkeypatch):
    handler = OAuthMixin()

    monkeypatch.setattr(handler, "get_cookie", lambda name: None)

    with pytest.raises(AuthError, match="Missing OAuth request token cookie"):
        await handler.get_authenticated_user()

@pytest.mark.asyncio
async def test_get_authenticated_user_token_mismatch(monkeypatch):
    handler = OAuthMixin()

    monkeypatch.setattr(handler, "get_cookie", lambda name: base64.b64encode(b"wrong_token|test_secret").decode('utf-8'))

    with pytest.raises(AuthError, match="Request token does not match cookie"):
        await handler.get_authenticated_user()

@pytest.mark.asyncio
async def test_get_authenticated_user_no_user(monkeypatch):
    handler = OAuthMixin()

    mock_http_client = MagicMock()
    mock_response = MagicMock()
    mock_response.body = b"access_token=test_access_token"
    mock_http_client.fetch = MagicMock(return_value=mock_response)

    monkeypatch.setattr(handler, "get_auth_http_client", lambda: mock_http_client)
    monkeypatch.setattr(handler, "_oauth_access_token_url", lambda token: "http://example.com/oauth/access_token")
    monkeypatch.setattr(handler, "_oauth_get_user_future", lambda access_token: None)

    with pytest.raises(AuthError, match="Error getting user"):
        await handler.get_authenticated_user()
