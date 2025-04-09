# file: tornado/auth.py:116-146
# asked: {"lines": [116, 117, 134, 136, 137, 139, 140, 141, 142, 143, 144, 146], "branches": [[141, 142], [141, 143]]}
# gained: {"lines": [116, 117], "branches": []}

import pytest
from tornado.web import RequestHandler
from tornado.httpclient import AsyncHTTPClient, HTTPResponse
from tornado.httputil import HTTPHeaders
from unittest.mock import MagicMock, patch
from typing import Dict, Any
from tornado.auth import OpenIdMixin  # Correct import path

class MockRequestHandler(RequestHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.request.arguments = {
            'openid.mode': [b'id_res'],
            'openid.ns.ax': [b'http://openid.net/srv/ax/1.0'],
            'openid.ax.type.email': [b'http://axschema.org/contact/email'],
            'openid.ax.value.email': [b'test@example.com'],
            'openid.ax.type.namePerson': [b'http://axschema.org/namePerson'],
            'openid.ax.value.namePerson': [b'Test User'],
            'openid.ax.type.namePerson/first': [b'http://axschema.org/namePerson/first'],
            'openid.ax.value.namePerson/first': [b'Test'],
            'openid.ax.type.namePerson/last': [b'http://axschema.org/namePerson/last'],
            'openid.ax.value.namePerson/last': [b'User'],
            'openid.ax.type.namePerson/friendly': [b'http://axschema.org/namePerson/friendly'],
            'openid.ax.value.namePerson/friendly': [b'testuser'],
            'openid.ax.type.pref/language': [b'http://axschema.org/pref/language'],
            'openid.ax.value.pref/language': [b'en'],
            'openid.claimed_id': [b'http://example.com/claimed_id']
        }

@pytest.mark.asyncio
async def test_get_authenticated_user(monkeypatch):
    mock_handler = MockRequestHandler(MagicMock(), MagicMock())
    mock_handler._OPENID_ENDPOINT = "http://example.com/openid"
    
    async def mock_fetch(url, method, body):
        assert url == "http://example.com/openid"
        assert method == "POST"
        assert "openid.mode=check_authentication" in body
        headers = HTTPHeaders({"Content-Type": "application/x-www-form-urlencoded"})
        return HTTPResponse(MagicMock(), 200, headers=headers, buffer=MagicMock())
    
    monkeypatch.setattr(AsyncHTTPClient, "fetch", mock_fetch)
    
    class TestOpenIdMixin(OpenIdMixin, MockRequestHandler):
        def get_auth_http_client(self):
            return AsyncHTTPClient()
    
    mixin = TestOpenIdMixin(MagicMock(), MagicMock())
    user = await mixin.get_authenticated_user()
    
    assert user['email'] == 'test@example.com'
    assert user['name'] == 'Test User'
    assert user['first_name'] == 'Test'
    assert user['last_name'] == 'User'
    assert user['username'] == 'testuser'
    assert user['locale'] == 'en'
    assert user['claimed_id'] == 'http://example.com/claimed_id'

@pytest.mark.asyncio
async def test_on_authentication_verified_invalid_response():
    mock_handler = MockRequestHandler(MagicMock(), MagicMock())
    
    class TestOpenIdMixin(OpenIdMixin, MockRequestHandler):
        pass
    
    mixin = TestOpenIdMixin(MagicMock(), MagicMock())
    
    response = HTTPResponse(MagicMock(), 200, buffer=MagicMock())
    response.body = b'is_valid:false'
    
    with pytest.raises(AuthError):
        mixin._on_authentication_verified(response)

@pytest.mark.asyncio
async def test_on_authentication_verified_valid_response():
    mock_handler = MockRequestHandler(MagicMock(), MagicMock())
    
    class TestOpenIdMixin(OpenIdMixin, MockRequestHandler):
        pass
    
    mixin = TestOpenIdMixin(MagicMock(), MagicMock())
    
    response = HTTPResponse(MagicMock(), 200, buffer=MagicMock())
    response.body = b'is_valid:true'
    
    user = mixin._on_authentication_verified(response)
    
    assert user['email'] == 'test@example.com'
    assert user['name'] == 'Test User'
    assert user['first_name'] == 'Test'
    assert user['last_name'] == 'User'
    assert user['username'] == 'testuser'
    assert user['locale'] == 'en'
    assert user['claimed_id'] == 'http://example.com/claimed_id'
