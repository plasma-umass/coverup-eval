# file: tornado/auth.py:859-921
# asked: {"lines": [859, 903, 904, 905, 906, 907, 908, 909, 910, 911, 915, 916, 917, 918, 919, 921], "branches": []}
# gained: {"lines": [859], "branches": []}

import pytest
from tornado.web import RequestHandler
from tornado.auth import GoogleOAuth2Mixin
from tornado.httpclient import AsyncHTTPClient, HTTPResponse
from tornado.httputil import HTTPHeaders
from tornado.escape import json_encode
from unittest.mock import patch, MagicMock

class MockHandler(RequestHandler, GoogleOAuth2Mixin):
    def initialize(self, settings):
        self._settings = settings

    def get_auth_http_client(self):
        return AsyncHTTPClient()

    @property
    def settings(self):
        return self._settings

@pytest.mark.asyncio
async def test_get_authenticated_user(monkeypatch):
    settings = {
        'google_oauth': {
            'key': 'test_client_id',
            'secret': 'test_client_secret'
        }
    }
    handler = MockHandler(application=None, request=None, settings=settings)

    async def mock_fetch(request, **kwargs):
        assert request.url == 'https://www.googleapis.com/oauth2/v4/token'
        assert kwargs['method'] == 'POST'
        assert kwargs['headers'] == {'Content-Type': 'application/x-www-form-urlencoded'}
        body = urllib.parse.parse_qs(kwargs['body'])
        assert body['redirect_uri'] == ['http://your.site.com/auth/google']
        assert body['code'] == ['test_code']
        assert body['client_id'] == ['test_client_id']
        assert body['client_secret'] == ['test_client_secret']
        assert body['grant_type'] == ['authorization_code']
        response = HTTPResponse(request, 200)
        response._body = json_encode({'access_token': 'test_access_token'})
        return response

    monkeypatch.setattr(AsyncHTTPClient, 'fetch', mock_fetch)

    result = await handler.get_authenticated_user('http://your.site.com/auth/google', 'test_code')
    assert result == {'access_token': 'test_access_token'}
