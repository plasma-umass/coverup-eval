# file tornado/auth.py:717-737
# lines [717, 733, 734, 735, 737]
# branches []

import pytest
from tornado.auth import TwitterMixin
from tornado.httpclient import HTTPResponse, HTTPRequest
from tornado.httputil import HTTPHeaders
from unittest.mock import patch, MagicMock

class MockHandler(TwitterMixin):
    def get_auth_http_client(self):
        return MagicMock()

    def _oauth_request_token_url(self, callback_uri=None):
        return "http://example.com/request_token"

    def _on_request_token(self, url, callback, response):
        pass

@pytest.mark.asyncio
async def test_authenticate_redirect(mocker):
    handler = MockHandler()

    mock_response = HTTPResponse(
        request=HTTPRequest("http://example.com/request_token"),
        code=200,
        headers=HTTPHeaders({"Content-Type": "application/json"}),
        buffer=None,
    )

    mock_http_client = handler.get_auth_http_client()
    mock_http_client.fetch = mocker.AsyncMock(return_value=mock_response)

    with patch.object(handler, '_on_request_token', return_value=None) as mock_on_request_token:
        await handler.authenticate_redirect(callback_uri="http://example.com/callback")
        mock_http_client.fetch.assert_called_once_with("http://example.com/request_token")
        mock_on_request_token.assert_called_once_with(handler._OAUTH_AUTHENTICATE_URL, None, mock_response)
