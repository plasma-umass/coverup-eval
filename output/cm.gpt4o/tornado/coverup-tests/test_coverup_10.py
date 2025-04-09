# file tornado/auth.py:339-383
# lines [339, 340, 357, 358, 359, 360, 361, 362, 363, 364, 365, 367, 368, 369, 370, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383]
# branches ['361->362', '361->363', '367->368', '367->369', '372->373', '372->374', '374->375', '374->376', '380->381', '380->382']

import pytest
from tornado.web import RequestHandler
from tornado.httpclient import AsyncHTTPClient, HTTPResponse, HTTPRequest
from tornado.escape import utf8
from tornado.auth import OAuthMixin, AuthError
from unittest.mock import patch, MagicMock
import base64

class MockHandler(RequestHandler, OAuthMixin):
    def get_argument(self, name, default=None):
        if name == "oauth_token":
            return "mock_oauth_token"
        elif name == "oauth_verifier":
            return "mock_oauth_verifier"
        return default

    def get_cookie(self, name):
        if name == "_oauth_request_token":
            return base64.b64encode(utf8("mock_oauth_token")) + b"|" + base64.b64encode(utf8("mock_secret"))

    def clear_cookie(self, name):
        pass

    def get_auth_http_client(self):
        return AsyncHTTPClient()

    async def _oauth_access_token_url(self, token):
        return "http://mock_oauth_access_token_url"

    async def _oauth_get_user_future(self, access_token):
        return {"name": "mock_user"}

def _oauth_parse_response(body):
    return {"access_token": "mock_access_token"}

@pytest.mark.asyncio
async def test_get_authenticated_user(mocker):
    handler = MockHandler(application=None, request=None)

    mock_http_client = MagicMock(spec=AsyncHTTPClient)
    mock_response = HTTPResponse(HTTPRequest("http://mock_oauth_access_token_url"), 200)
    mock_response.body = b"access_token=mock_access_token"
    mock_http_client.fetch = MagicMock(return_value=mock_response)

    with patch.object(handler, 'get_auth_http_client', return_value=mock_http_client):
        user = await handler.get_authenticated_user()

    assert user["access_token"] == {"access_token": "mock_access_token"}
    assert user["name"] == "mock_user"
