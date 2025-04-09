# file tornado/httpclient.py:309-312
# lines [309, 312]
# branches []

import pytest
from tornado.httpclient import AsyncHTTPClient, HTTPRequest, HTTPResponse
from typing import Callable
from unittest.mock import create_autospec

class MockAsyncHTTPClient(AsyncHTTPClient):
    def fetch_impl(self, request: "HTTPRequest", callback: Callable[[HTTPResponse], None]) -> None:
        response = HTTPResponse(request, 200)
        callback(response)

@pytest.fixture
def mock_http_client(mocker):
    client = MockAsyncHTTPClient()
    mocker.patch.object(AsyncHTTPClient, 'fetch_impl', client.fetch_impl)
    return client

def test_fetch_impl(mock_http_client):
    request = HTTPRequest(url='http://example.com')
    callback = create_autospec(lambda response: None)

    mock_http_client.fetch_impl(request, callback)

    # Verify that the callback was called with an HTTPResponse object with a 200 status code
    callback.assert_called_once()
    response = callback.call_args[0][0]
    assert isinstance(response, HTTPResponse)
    assert response.code == 200
