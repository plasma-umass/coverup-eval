# file: tornado/auth.py:610-664
# asked: {"lines": [610, 613, 614, 650, 651, 652, 653, 655, 656, 657, 658, 659, 660, 663, 664], "branches": [[651, 652], [651, 655], [655, 656], [655, 657], [658, 659], [658, 663]]}
# gained: {"lines": [610, 613, 614], "branches": []}

import pytest
from tornado.auth import OAuth2Mixin
from tornado.httpclient import AsyncHTTPClient, HTTPResponse, HTTPRequest
from tornado.escape import json_encode
from unittest.mock import patch, MagicMock

class TestOAuth2Mixin:
    
    @pytest.mark.asyncio
    async def test_oauth2_request_with_access_token_and_post_args(self, monkeypatch):
        class TestHandler(OAuth2Mixin):
            def get_auth_http_client(self):
                return AsyncHTTPClient()
        
        handler = TestHandler()
        
        async def mock_fetch(request, **kwargs):
            assert request.url == "https://example.com/?access_token=test_token"
            assert kwargs['method'] == "POST"
            assert kwargs['body'] == "key=value"
            return HTTPResponse(request, 200, buffer=json_encode({"result": "success"}).encode())
        
        monkeypatch.setattr(AsyncHTTPClient, "fetch", mock_fetch)
        
        response = await handler.oauth2_request(
            "https://example.com/",
            access_token="test_token",
            post_args={"key": "value"}
        )
        
        assert response == {"result": "success"}
    
    @pytest.mark.asyncio
    async def test_oauth2_request_with_access_token_no_post_args(self, monkeypatch):
        class TestHandler(OAuth2Mixin):
            def get_auth_http_client(self):
                return AsyncHTTPClient()
        
        handler = TestHandler()
        
        async def mock_fetch(request, **kwargs):
            assert request.url == "https://example.com/?access_token=test_token"
            return HTTPResponse(request, 200, buffer=json_encode({"result": "success"}).encode())
        
        monkeypatch.setattr(AsyncHTTPClient, "fetch", mock_fetch)
        
        response = await handler.oauth2_request(
            "https://example.com/",
            access_token="test_token"
        )
        
        assert response == {"result": "success"}
    
    @pytest.mark.asyncio
    async def test_oauth2_request_no_access_token_with_args(self, monkeypatch):
        class TestHandler(OAuth2Mixin):
            def get_auth_http_client(self):
                return AsyncHTTPClient()
        
        handler = TestHandler()
        
        async def mock_fetch(request, **kwargs):
            assert request.url == "https://example.com/?arg1=value1&arg2=value2"
            return HTTPResponse(request, 200, buffer=json_encode({"result": "success"}).encode())
        
        monkeypatch.setattr(AsyncHTTPClient, "fetch", mock_fetch)
        
        response = await handler.oauth2_request(
            "https://example.com/",
            arg1="value1",
            arg2="value2"
        )
        
        assert response == {"result": "success"}
    
    @pytest.mark.asyncio
    async def test_oauth2_request_no_access_token_no_args(self, monkeypatch):
        class TestHandler(OAuth2Mixin):
            def get_auth_http_client(self):
                return AsyncHTTPClient()
        
        handler = TestHandler()
        
        async def mock_fetch(request, **kwargs):
            assert request.url == "https://example.com/"
            return HTTPResponse(request, 200, buffer=json_encode({"result": "success"}).encode())
        
        monkeypatch.setattr(AsyncHTTPClient, "fetch", mock_fetch)
        
        response = await handler.oauth2_request("https://example.com/")
        
        assert response == {"result": "success"}
