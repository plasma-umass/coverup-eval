# file: tornado/auth.py:1039-1099
# asked: {"lines": [1039, 1042, 1043, 1096, 1097, 1098], "branches": []}
# gained: {"lines": [1039, 1042, 1043], "branches": []}

import pytest
from tornado.auth import FacebookGraphMixin, OAuth2Mixin
from tornado.httpclient import AsyncHTTPClient
from unittest.mock import patch, MagicMock

class TestFacebookGraphMixin:
    
    @pytest.mark.asyncio
    async def test_facebook_request_get(self, monkeypatch):
        class TestHandler(FacebookGraphMixin):
            _FACEBOOK_BASE_URL = "https://graph.facebook.com"
        
        handler = TestHandler()
        
        async def mock_oauth2_request(url, access_token=None, post_args=None, **args):
            assert url == "https://graph.facebook.com/test_path"
            assert access_token == "test_token"
            assert post_args is None
            assert args == {"arg1": "value1"}
            return {"result": "success"}
        
        monkeypatch.setattr(handler, "oauth2_request", mock_oauth2_request)
        
        response = await handler.facebook_request(
            "/test_path", access_token="test_token", arg1="value1"
        )
        
        assert response == {"result": "success"}
    
    @pytest.mark.asyncio
    async def test_facebook_request_post(self, monkeypatch):
        class TestHandler(FacebookGraphMixin):
            _FACEBOOK_BASE_URL = "https://graph.facebook.com"
        
        handler = TestHandler()
        
        async def mock_oauth2_request(url, access_token=None, post_args=None, **args):
            assert url == "https://graph.facebook.com/test_path"
            assert access_token == "test_token"
            assert post_args == {"key": "value"}
            assert args == {"arg1": "value1"}
            return {"result": "success"}
        
        monkeypatch.setattr(handler, "oauth2_request", mock_oauth2_request)
        
        response = await handler.facebook_request(
            "/test_path", access_token="test_token", post_args={"key": "value"}, arg1="value1"
        )
        
        assert response == {"result": "success"}
