# file tornado/auth.py:339-383
# lines [339, 340, 357, 358, 359, 360, 361, 362, 363, 364, 365, 367, 368, 369, 370, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383]
# branches ['361->362', '361->363', '367->368', '367->369', '372->373', '372->374', '374->375', '374->376', '380->381', '380->382']

import base64
import pytest
from tornado.auth import OAuthMixin, AuthError
from tornado import escape, httpclient
from unittest.mock import MagicMock, patch

class DummyHandler(OAuthMixin):
    def get_argument(self, name, default=None):
        if name == "oauth_token":
            return "dummy_oauth_token"
        elif name == "oauth_verifier":
            return "dummy_oauth_verifier"
        return default

    def get_cookie(self, name):
        if name == "_oauth_request_token":
            token = base64.b64encode(b"dummy_oauth_token").decode()
            secret = base64.b64encode(b"dummy_oauth_secret").decode()
            return f"{token}|{secret}"
        return None

    def clear_cookie(self, name):
        pass

    def get_auth_http_client(self):
        return MagicMock(spec=httpclient.AsyncHTTPClient)

    async def _oauth_access_token_url(self, token):
        return "http://dummy_access_token_url"

    async def _oauth_get_user_future(self, access_token):
        return {"name": "Dummy User", "access_token": access_token}

@pytest.mark.asyncio
async def test_get_authenticated_user():
    handler = DummyHandler()

    with patch.object(handler, '_oauth_access_token_url') as mock_access_token_url, \
         patch.object(handler, '_oauth_get_user_future') as mock_get_user_future, \
         patch.object(httpclient.AsyncHTTPClient, 'fetch') as mock_fetch:

        mock_access_token_url.return_value = "http://dummy_access_token_url"
        mock_get_user_future.return_value = {"name": "Dummy User"}
        mock_fetch.return_value = MagicMock(body="access_token=dummy_access_token")

        user = await handler.get_authenticated_user()

        assert user["name"] == "Dummy User"
        assert user["access_token"] == {"access_token": "dummy_access_token"}

        mock_access_token_url.assert_called_once_with({'key': b'dummy_oauth_token', 'secret': b'dummy_oauth_secret', 'verifier': 'dummy_oauth_verifier'})
        mock_get_user_future.assert_called_once_with({"access_token": "dummy_access_token"})
        mock_fetch.assert_called_once_with("http://dummy_access_token_url")

@pytest.mark.asyncio
async def test_get_authenticated_user_missing_cookie():
    handler = DummyHandler()
    handler.get_cookie = MagicMock(return_value=None)

    with pytest.raises(AuthError) as exc_info:
        await handler.get_authenticated_user()
    assert str(exc_info.value) == "Missing OAuth request token cookie"

@pytest.mark.asyncio
async def test_get_authenticated_user_mismatch_token():
    handler = DummyHandler()
    handler.get_cookie = MagicMock(return_value=base64.b64encode(b"mismatched_token").decode() + "|" + base64.b64encode(b"dummy_oauth_secret").decode())

    with pytest.raises(AuthError) as exc_info:
        await handler.get_authenticated_user()
    assert str(exc_info.value) == "Request token does not match cookie"

@pytest.mark.asyncio
async def test_get_authenticated_user_error_getting_user():
    handler = DummyHandler()

    with patch.object(handler, '_oauth_access_token_url') as mock_access_token_url, \
         patch.object(handler, '_oauth_get_user_future') as mock_get_user_future, \
         patch.object(httpclient.AsyncHTTPClient, 'fetch') as mock_fetch:

        mock_access_token_url.return_value = "http://dummy_access_token_url"
        mock_get_user_future.return_value = None
        mock_fetch.return_value = MagicMock(body="access_token=dummy_access_token")

        with pytest.raises(AuthError) as exc_info:
            await handler.get_authenticated_user()
        assert str(exc_info.value) == "Error getting user"
