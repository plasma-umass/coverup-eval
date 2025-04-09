# file tornado/auth.py:717-737
# lines [717, 733, 734, 735, 737]
# branches []

import pytest
from tornado.auth import TwitterMixin
from tornado.httpclient import HTTPResponse, HTTPRequest
from unittest.mock import Mock

class DummyTwitterMixin(TwitterMixin):
    def _oauth_request_token_url(self, callback_uri=None):
        return 'http://dummy_oauth_request_token_url'

    def _on_request_token(self, authorize_url, callback, response):
        pass

    def get_auth_http_client(self):
        return Mock()

@pytest.mark.asyncio
async def test_authenticate_redirect(mocker):
    # Mock the http client and its fetch method
    http_client_mock = mocker.Mock()
    http_client_mock.fetch = mocker.AsyncMock(return_value=HTTPResponse(HTTPRequest(url='http://dummy_url'), 200))

    # Patch the get_auth_http_client method to return our mock
    mocker.patch.object(DummyTwitterMixin, 'get_auth_http_client', return_value=http_client_mock)

    # Patch the _oauth_request_token_url and _on_request_token to prevent actual network calls
    mocker.patch.object(DummyTwitterMixin, '_oauth_request_token_url', return_value='http://dummy_oauth_request_token_url')
    mocker.patch.object(DummyTwitterMixin, '_on_request_token')

    # Create an instance of our DummyTwitterMixin
    mixin_instance = DummyTwitterMixin()

    # Call the method under test
    await mixin_instance.authenticate_redirect(callback_uri='http://dummy_callback_uri')

    # Assert that the http client's fetch method was called with the correct URL
    http_client_mock.fetch.assert_called_once_with('http://dummy_oauth_request_token_url')

    # Assert that the _on_request_token method was called with the correct parameters
    mixin_instance._on_request_token.assert_called_once_with(
        mixin_instance._OAUTH_AUTHENTICATE_URL,
        None,
        http_client_mock.fetch.return_value
    )
