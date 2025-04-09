# file tornado/auth.py:116-146
# lines [116, 117, 134, 136, 137, 139, 140, 141, 142, 143, 144, 146]
# branches ['141->142', '141->143']

import pytest
from tornado.auth import OpenIdMixin
from tornado.httpclient import AsyncHTTPClient, HTTPResponse
from tornado.httputil import HTTPHeaders
from unittest.mock import create_autospec, Mock
from typing import Any, Dict, Optional

class DummyHandler(OpenIdMixin):
    def __init__(self, request):
        self.request = request

    def get_auth_http_client(self) -> AsyncHTTPClient:
        return create_autospec(AsyncHTTPClient, instance=True)

    async def _on_authentication_verified(self, response: HTTPResponse) -> Dict[str, Any]:
        return {}

@pytest.mark.asyncio
async def test_get_authenticated_user(mocker):
    # Mock the request object with necessary attributes
    request = mocker.Mock()
    request.arguments = {
        'openid.mode': [b'checkid_setup'],
        'other': [b'value']
    }

    # Create an instance of the DummyHandler with the mocked request
    handler = DummyHandler(request)

    # Mock the AsyncHTTPClient and its fetch method
    http_client = create_autospec(AsyncHTTPClient, instance=True)
    http_client.fetch = mocker.AsyncMock()

    # Mock the HTTPResponse to be returned by the fetch method
    response = HTTPResponse(request, 200, headers=HTTPHeaders(), buffer=mocker.Mock())
    http_client.fetch.return_value = response

    # Mock the _on_authentication_verified method to return a known dict
    expected_user_data = {'authenticated': True}
    handler._on_authentication_verified = mocker.AsyncMock(return_value=expected_user_data)

    # Call the get_authenticated_user method
    user_data = await handler.get_authenticated_user(http_client)

    # Assert that the fetch method was called with the correct arguments
    args = {
        'openid.mode': b'check_authentication',
        'other': b'value'
    }
    http_client.fetch.assert_called_once_with(
        handler._OPENID_ENDPOINT,
        method="POST",
        body=urllib.parse.urlencode(args)
    )

    # Assert that the _on_authentication_verified method was called with the response
    handler._on_authentication_verified.assert_called_once_with(response)

    # Assert that the returned user data is as expected
    assert user_data == expected_user_data

    # Clean up mocks
    mocker.stopall()
