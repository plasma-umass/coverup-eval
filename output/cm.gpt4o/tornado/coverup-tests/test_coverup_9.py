# file tornado/auth.py:932-1037
# lines [932, 938, 985, 986, 987, 988, 989, 990, 993, 994, 996, 997, 999, 1000, 1002, 1003, 1004, 1005, 1007, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1020, 1021, 1023, 1024, 1025, 1031, 1032, 1033, 1034, 1037]
# branches ['996->997', '996->999', '1020->1021', '1020->1023', '1024->1025', '1024->1031']

import pytest
from tornado.auth import FacebookGraphMixin
from tornado.web import RequestHandler
from tornado.escape import json_encode
from unittest.mock import patch, AsyncMock
import hmac
import hashlib

class MockFacebookGraphMixin(FacebookGraphMixin, RequestHandler):
    def get_auth_http_client(self):
        return AsyncMock()

    def _oauth_request_token_url(self, **args):
        return "https://graph.facebook.com/oauth/access_token?" + "&".join(f"{k}={v}" for k, v in args.items())

    async def facebook_request(self, path, access_token, appsecret_proof, fields):
        return {
            "id": "12345",
            "name": "Test User",
            "first_name": "Test",
            "last_name": "User",
            "locale": "en_US",
            "picture": {"data": {"url": "http://example.com/picture.jpg"}},
            "link": "http://facebook.com/testuser",
        }

@pytest.mark.asyncio
async def test_get_authenticated_user(mocker):
    mock_handler = MockFacebookGraphMixin()
    mock_handler.settings = {
        "facebook_api_key": "fake_api_key",
        "facebook_secret": "fake_secret"
    }

    mock_response = AsyncMock()
    mock_response.body = json_encode({
        "access_token": "fake_access_token",
        "expires_in": 3600
    }).encode('utf-8')

    mock_http_client = mock_handler.get_auth_http_client()
    mock_http_client.fetch.return_value = mock_response

    user = await mock_handler.get_authenticated_user(
        redirect_uri='/auth/facebookgraph/',
        client_id=mock_handler.settings["facebook_api_key"],
        client_secret=mock_handler.settings["facebook_secret"],
        code="fake_code"
    )

    assert user is not None
    assert user["access_token"] == "fake_access_token"
    assert user["session_expires"] == "3600"
    assert user["id"] == "12345"
    assert user["name"] == "Test User"
    assert user["first_name"] == "Test"
    assert user["last_name"] == "User"
    assert user["locale"] == "en_US"
    assert user["picture"]["data"]["url"] == "http://example.com/picture.jpg"
    assert user["link"] == "http://facebook.com/testuser"
