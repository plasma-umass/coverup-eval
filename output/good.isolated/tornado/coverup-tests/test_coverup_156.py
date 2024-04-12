# file tornado/httpclient.py:314-336
# lines [314, 315, 336]
# branches []

import pytest
from tornado.httpclient import AsyncHTTPClient

@pytest.fixture
def reset_async_http_client(mocker):
    # Mock the configure method to prevent actual changes to the AsyncHTTPClient configuration
    mocker.patch.object(AsyncHTTPClient, 'configure')

def test_async_http_client_configure(reset_async_http_client):
    class MockAsyncHTTPClient(AsyncHTTPClient):
        pass

    # Configure with a class object
    AsyncHTTPClient.configure(MockAsyncHTTPClient, max_clients=10)
    AsyncHTTPClient.configure.assert_called_once_with(MockAsyncHTTPClient, max_clients=10)

    # Reset mock to test the next configure call
    AsyncHTTPClient.configure.reset_mock()

    # Configure with a fully-qualified class name
    AsyncHTTPClient.configure('tornado.httpclient.AsyncHTTPClient', max_clients=20)
    AsyncHTTPClient.configure.assert_called_once_with('tornado.httpclient.AsyncHTTPClient', max_clients=20)

    # Reset mock to test the next configure call
    AsyncHTTPClient.configure.reset_mock()

    # Configure with None to use the default
    AsyncHTTPClient.configure(None)
    AsyncHTTPClient.configure.assert_called_once_with(None)
