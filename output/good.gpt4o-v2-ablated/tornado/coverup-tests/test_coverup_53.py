# file: tornado/auth.py:1039-1099
# asked: {"lines": [1039, 1042, 1043, 1096, 1097, 1098], "branches": []}
# gained: {"lines": [1039, 1042, 1043], "branches": []}

import pytest
from tornado.auth import FacebookGraphMixin
from tornado.web import RequestHandler
from unittest.mock import patch, AsyncMock

class MockHandler(RequestHandler, FacebookGraphMixin):
    _FACEBOOK_BASE_URL = "https://graph.facebook.com"

@pytest.mark.asyncio
async def test_facebook_request_get(monkeypatch):
    handler = MockHandler(application=None, request=None)
    
    async def mock_oauth2_request(url, access_token=None, post_args=None, **args):
        assert url == "https://graph.facebook.com/me"
        assert access_token == "dummy_access_token"
        assert post_args is None
        assert args == {"fields": "id,name"}
        return {"id": "123", "name": "Test User"}
    
    monkeypatch.setattr(handler, "oauth2_request", mock_oauth2_request)
    
    response = await handler.facebook_request("/me", access_token="dummy_access_token", fields="id,name")
    assert response == {"id": "123", "name": "Test User"}

@pytest.mark.asyncio
async def test_facebook_request_post(monkeypatch):
    handler = MockHandler(application=None, request=None)
    
    async def mock_oauth2_request(url, access_token=None, post_args=None, **args):
        assert url == "https://graph.facebook.com/me/feed"
        assert access_token == "dummy_access_token"
        assert post_args == {"message": "Hello World"}
        assert args == {}
        return {"id": "post_123"}
    
    monkeypatch.setattr(handler, "oauth2_request", mock_oauth2_request)
    
    response = await handler.facebook_request("/me/feed", access_token="dummy_access_token", post_args={"message": "Hello World"})
    assert response == {"id": "post_123"}

@pytest.mark.asyncio
async def test_facebook_request_no_access_token(monkeypatch):
    handler = MockHandler(application=None, request=None)
    
    async def mock_oauth2_request(url, access_token=None, post_args=None, **args):
        assert url == "https://graph.facebook.com/me"
        assert access_token is None
        assert post_args is None
        assert args == {}
        return {"id": "123", "name": "Test User"}
    
    monkeypatch.setattr(handler, "oauth2_request", mock_oauth2_request)
    
    response = await handler.facebook_request("/me")
    assert response == {"id": "123", "name": "Test User"}
