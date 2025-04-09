# file: tornado/auth.py:610-664
# asked: {"lines": [610, 613, 614, 650, 651, 652, 653, 655, 656, 657, 658, 659, 660, 663, 664], "branches": [[651, 652], [651, 655], [655, 656], [655, 657], [658, 659], [658, 663]]}
# gained: {"lines": [610, 613, 614], "branches": []}

import pytest
from tornado.auth import OAuth2Mixin
from tornado.httpclient import AsyncHTTPClient, HTTPResponse, HTTPRequest
from tornado.escape import json_encode
from unittest.mock import patch, MagicMock

class TestOAuth2Mixin(OAuth2Mixin):
    def get_auth_http_client(self):
        return AsyncHTTPClient()

@pytest.mark.asyncio
async def test_oauth2_request_with_access_token_and_post_args(monkeypatch):
    mixin = TestOAuth2Mixin()
    url = "http://example.com"
    access_token = "test_token"
    post_args = {"key": "value"}
    expected_url = f"{url}?access_token={access_token}"
    expected_body = urllib.parse.urlencode(post_args)
    response_data = {"status": "success"}
    
    async def mock_fetch(request, **kwargs):
        assert request.url == expected_url
        assert request.method == "POST"
        assert request.body == expected_body
        return HTTPResponse(request, 200, buffer=json_encode(response_data))
    
    monkeypatch.setattr(AsyncHTTPClient, "fetch", mock_fetch)
    
    response = await mixin.oauth2_request(url, access_token=access_token, post_args=post_args)
    assert response == response_data

@pytest.mark.asyncio
async def test_oauth2_request_with_access_token_without_post_args(monkeypatch):
    mixin = TestOAuth2Mixin()
    url = "http://example.com"
    access_token = "test_token"
    expected_url = f"{url}?access_token={access_token}"
    response_data = {"status": "success"}
    
    async def mock_fetch(request, **kwargs):
        assert request.url == expected_url
        assert request.method == "GET"
        return HTTPResponse(request, 200, buffer=json_encode(response_data))
    
    monkeypatch.setattr(AsyncHTTPClient, "fetch", mock_fetch)
    
    response = await mixin.oauth2_request(url, access_token=access_token)
    assert response == response_data

@pytest.mark.asyncio
async def test_oauth2_request_without_access_token_with_post_args(monkeypatch):
    mixin = TestOAuth2Mixin()
    url = "http://example.com"
    post_args = {"key": "value"}
    expected_body = urllib.parse.urlencode(post_args)
    response_data = {"status": "success"}
    
    async def mock_fetch(request, **kwargs):
        assert request.url == url
        assert request.method == "POST"
        assert request.body == expected_body
        return HTTPResponse(request, 200, buffer=json_encode(response_data))
    
    monkeypatch.setattr(AsyncHTTPClient, "fetch", mock_fetch)
    
    response = await mixin.oauth2_request(url, post_args=post_args)
    assert response == response_data

@pytest.mark.asyncio
async def test_oauth2_request_without_access_token_or_post_args(monkeypatch):
    mixin = TestOAuth2Mixin()
    url = "http://example.com"
    response_data = {"status": "success"}
    
    async def mock_fetch(request, **kwargs):
        assert request.url == url
        assert request.method == "GET"
        return HTTPResponse(request, 200, buffer=json_encode(response_data))
    
    monkeypatch.setattr(AsyncHTTPClient, "fetch", mock_fetch)
    
    response = await mixin.oauth2_request(url)
    assert response == response_data
