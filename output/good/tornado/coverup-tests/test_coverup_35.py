# file tornado/auth.py:859-921
# lines [859, 903, 904, 905, 906, 907, 908, 909, 910, 911, 915, 916, 917, 918, 919, 921]
# branches []

import pytest
from tornado.auth import GoogleOAuth2Mixin
from tornado.web import RequestHandler
from tornado.httpclient import HTTPResponse, HTTPRequest
from unittest.mock import Mock
from tornado.escape import json_encode

class MockHTTPClient:
    def __init__(self, response):
        self.response = response

    async def fetch(self, request, **kwargs):
        return self.response

@pytest.mark.asyncio
async def test_get_authenticated_user(mocker):
    # Mock the settings with OAuth credentials
    settings = {
        'google_oauth': {
            'key': 'test_client_id',
            'secret': 'test_client_secret'
        }
    }

    # Mock the RequestHandler to include settings
    mock_handler = mocker.MagicMock(spec=RequestHandler)
    mock_handler.settings = settings

    # Mock the response from the OAuth server
    mock_response = HTTPResponse(
        request=HTTPRequest(url='http://example.com'),
        code=200,
        buffer=Mock(),
        effective_url='http://example.com',
        headers={},
        reason='OK',
        body=json_encode({
            'access_token': 'test_access_token',
            'token_type': 'Bearer',
            'expires_in': 3600,
            'refresh_token': 'test_refresh_token',
        })
    )

    # Mock the HTTP client to return the mock response
    mock_http_client = MockHTTPClient(mock_response)
    mocker.patch.object(GoogleOAuth2Mixin, 'get_auth_http_client', return_value=mock_http_client)

    # Create a mixin instance and attach the mock handler
    mixin = GoogleOAuth2Mixin()
    mixin._OAUTH_SETTINGS_KEY = 'google_oauth'
    mixin._OAUTH_ACCESS_TOKEN_URL = 'http://example.com/token'
    mixin.get_auth_http_client = mock_http_client.fetch
    mixin.request = mock_handler.request

    # Call the method under test
    user = await mixin.get_authenticated_user(
        redirect_uri='http://your.site.com/auth/google',
        code='test_code'
    )

    # Assertions to verify the postconditions
    assert user['access_token'] == 'test_access_token'
    assert user['token_type'] == 'Bearer'
    assert user['expires_in'] == 3600
    assert user['refresh_token'] == 'test_refresh_token'
