# file: tornado/auth.py:932-1037
# asked: {"lines": [932, 938, 985, 986, 987, 988, 989, 990, 993, 994, 996, 997, 999, 1000, 1002, 1003, 1004, 1005, 1007, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1020, 1021, 1023, 1024, 1025, 1031, 1032, 1033, 1034, 1037], "branches": [[996, 997], [996, 999], [1020, 1021], [1020, 1023], [1024, 1025], [1024, 1031]]}
# gained: {"lines": [932, 938], "branches": []}

import pytest
from tornado.auth import FacebookGraphMixin
from tornado.httpclient import AsyncHTTPClient, HTTPResponse, HTTPRequest
from tornado.escape import json_encode
from unittest.mock import patch, MagicMock

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
            "link": "http://facebook.com/testuser"
        }

@pytest.mark.asyncio
async def test_get_authenticated_user(monkeypatch):
    async def mock_fetch(request):
        return HTTPResponse(
            request, 200,
            buffer=json_encode({
                "access_token": "test_access_token",
                "expires_in": 3600
            }).encode('utf-8')
        )

    monkeypatch.setattr(AsyncHTTPClient, "fetch", mock_fetch)

    mixin = MockFacebookGraphMixin()
    user = await mixin.get_authenticated_user(
        redirect_uri="http://example.com/redirect",
        client_id="test_client_id",
        client_secret="test_client_secret",
        code="test_code",
        extra_fields={"email": "test@example.com"}
    )

    assert user is not None
    assert user["access_token"] == "test_access_token"
    assert user["session_expires"] == "3600"
    assert user["id"] == "12345"
    assert user["name"] == "Test User"
    assert user["first_name"] == "Test"
    assert user["last_name"] == "User"
    assert user["locale"] == "en_US"
    assert user["picture"] == {"data": {"url": "http://example.com/picture.jpg"}}
    assert user["link"] == "http://facebook.com/testuser"
