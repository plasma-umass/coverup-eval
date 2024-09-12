# file: tornado/auth.py:717-737
# asked: {"lines": [717, 733, 734, 735, 737], "branches": []}
# gained: {"lines": [717], "branches": []}

import pytest
from tornado.auth import TwitterMixin
from tornado.httpclient import HTTPResponse, HTTPRequest, AsyncHTTPClient
from tornado.concurrent import Future
from unittest.mock import patch, MagicMock

class MockHandler(TwitterMixin):
    def get_auth_http_client(self):
        return AsyncHTTPClient()

    def _oauth_request_token_url(self, callback_uri=None):
        return "http://example.com/request_token"

    def _on_request_token(self, url, callback, response):
        pass

@pytest.mark.asyncio
async def test_authenticate_redirect(monkeypatch):
    handler = MockHandler()

    # Mock the HTTP response
    mock_response = HTTPResponse(HTTPRequest("http://example.com"), 200)
    future = Future()
    future.set_result(mock_response)

    async def mock_fetch(request):
        return future

    # Patch the fetch method of the HTTP client
    monkeypatch.setattr(AsyncHTTPClient, "fetch", mock_fetch)

    # Patch the _on_request_token method to verify it gets called
    with patch.object(handler, '_on_request_token', wraps=handler._on_request_token) as mock_on_request_token:
        await handler.authenticate_redirect(callback_uri="http://example.com/callback")
        mock_on_request_token.assert_called_once_with(handler._OAUTH_AUTHENTICATE_URL, None, mock_response)
