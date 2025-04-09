# file: tornado/httpclient.py:89-110
# asked: {"lines": [], "branches": [[99, 104]]}
# gained: {"lines": [], "branches": [[99, 104]]}

import pytest
from tornado.httpclient import HTTPClient, AsyncHTTPClient
from tornado.ioloop import IOLoop

@pytest.fixture
def mock_async_http_client(mocker):
    mocker.patch('tornado.httpclient.AsyncHTTPClient', autospec=True)
    return AsyncHTTPClient

def test_http_client_with_default_async_client_class(mock_async_http_client):
    client = HTTPClient()
    assert not client._closed
    assert isinstance(client._async_client, mock_async_http_client)

def test_http_client_with_custom_async_client_class():
    class CustomAsyncHTTPClient(AsyncHTTPClient):
        pass

    client = HTTPClient(async_client_class=CustomAsyncHTTPClient)
    assert not client._closed
    assert isinstance(client._async_client, CustomAsyncHTTPClient)
