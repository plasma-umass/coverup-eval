# file: tornado/auth.py:932-1037
# asked: {"lines": [932, 938, 985, 986, 987, 988, 989, 990, 993, 994, 996, 997, 999, 1000, 1002, 1003, 1004, 1005, 1007, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1020, 1021, 1023, 1024, 1025, 1031, 1032, 1033, 1034, 1037], "branches": [[996, 997], [996, 999], [1020, 1021], [1020, 1023], [1024, 1025], [1024, 1031]]}
# gained: {"lines": [932, 938], "branches": []}

import pytest
from tornado.auth import FacebookGraphMixin
from tornado.httpclient import AsyncHTTPClient, HTTPResponse, HTTPRequest
from tornado.escape import json_encode
from unittest.mock import patch, MagicMock
import hmac
import hashlib

class MockFacebookGraphMixin(FacebookGraphMixin):
    def get_auth_http_client(self):
        return AsyncHTTPClient()

    async def facebook_request(self, path, access_token, appsecret_proof, fields):
        return {
            "id": "12345",
            "name": "Test User",
            "first_name": "Test",
            "last_name": "User",
            "locale": "en_US",
            "picture": {"data": {"url": "http://example.com/picture.jpg"}},
            "link": "http://example.com/profile",
        }

@pytest.mark.asyncio
async def test_get_authenticated_user(monkeypatch):
    async def mock_fetch(request):
        body = json_encode({
            "access_token": "mock_access_token",
            "expires_in": 3600
        })
        response = HTTPResponse(HTTPRequest(request.url), 200, buffer=body)
        return response

    monkeypatch.setattr(AsyncHTTPClient, "fetch", mock_fetch)

    mixin = MockFacebookGraphMixin()
    result = await mixin.get_authenticated_user(
        redirect_uri="http://example.com/auth",
        client_id="mock_client_id",
        client_secret="mock_client_secret",
        code="mock_code",
        extra_fields={"email"}
    )

    assert result is not None
    assert result["access_token"] == "mock_access_token"
    assert result["session_expires"] == "3600"
    assert result["id"] == "12345"
    assert result["name"] == "Test User"
    assert result["first_name"] == "Test"
    assert result["last_name"] == "User"
    assert result["locale"] == "en_US"
    assert result["picture"] == {"data": {"url": "http://example.com/picture.jpg"}}
    assert result["link"] == "http://example.com/profile"
    assert "email" in result
