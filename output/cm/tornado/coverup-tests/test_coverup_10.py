# file tornado/auth.py:290-337
# lines [290, 292, 293, 294, 323, 324, 325, 326, 327, 328, 329, 330, 331, 335, 336, 337]
# branches ['323->324', '323->325', '325->326', '325->327', '328->329', '328->335']

import pytest
from tornado.auth import OAuthMixin
from tornado import httpclient
from unittest.mock import AsyncMock, MagicMock

class DummyOAuthMixin(OAuthMixin):
    _OAUTH_NO_CALLBACKS = False
    _OAUTH_VERSION = "1.0a"
    _OAUTH_AUTHORIZE_URL = "http://example.com/authorize"

    def _oauth_request_token_url(self, callback_uri=None, extra_params=None):
        return "http://example.com/request_token"

    def _on_request_token(self, url, callback_uri, response):
        pass

    def get_auth_http_client(self):
        return httpclient.AsyncHTTPClient()

@pytest.mark.asyncio
async def test_authorize_redirect_with_callback_uri(mocker):
    # Mock the http_client.fetch method
    mock_fetch = AsyncMock()
    mock_fetch.return_value = MagicMock()
    mocker.patch.object(httpclient.AsyncHTTPClient, 'fetch', mock_fetch)

    # Create an instance of the DummyOAuthMixin
    oauth_mixin = DummyOAuthMixin()

    # Call the authorize_redirect method with a callback_uri
    await oauth_mixin.authorize_redirect(callback_uri="http://example.com/callback")

    # Assert that the fetch method was called with the correct URL
    mock_fetch.assert_called_once_with("http://example.com/request_token")

@pytest.mark.asyncio
async def test_authorize_redirect_no_callback_uri(mocker):
    # Mock the http_client.fetch method
    mock_fetch = AsyncMock()
    mock_fetch.return_value = MagicMock()
    mocker.patch.object(httpclient.AsyncHTTPClient, 'fetch', mock_fetch)

    # Create an instance of the DummyOAuthMixin
    oauth_mixin = DummyOAuthMixin()

    # Call the authorize_redirect method without a callback_uri
    await oauth_mixin.authorize_redirect()

    # Assert that the fetch method was called with the correct URL
    mock_fetch.assert_called_once_with("http://example.com/request_token")

@pytest.mark.asyncio
async def test_authorize_redirect_raises_exception_for_no_callbacks(mocker):
    # Mock the http_client.fetch method
    mocker.patch.object(httpclient.AsyncHTTPClient, 'fetch', AsyncMock())

    # Create an instance of the DummyOAuthMixin with _OAUTH_NO_CALLBACKS set to True
    oauth_mixin = DummyOAuthMixin()
    oauth_mixin._OAUTH_NO_CALLBACKS = True

    # Assert that an exception is raised when calling authorize_redirect with a callback_uri
    with pytest.raises(Exception) as exc_info:
        await oauth_mixin.authorize_redirect(callback_uri="http://example.com/callback")
    assert str(exc_info.value) == "This service does not support oauth_callback"
