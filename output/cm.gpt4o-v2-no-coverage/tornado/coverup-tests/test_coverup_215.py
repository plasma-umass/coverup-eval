# file: tornado/httpclient.py:89-110
# asked: {"lines": [], "branches": [[99, 104]]}
# gained: {"lines": [], "branches": [[99, 104]]}

import pytest
from tornado.httpclient import HTTPClient, AsyncHTTPClient
from tornado.ioloop import IOLoop

@pytest.fixture
def mock_async_http_client(mocker):
    mocker.patch('tornado.httpclient.AsyncHTTPClient.__new__', side_effect=lambda cls, *args, **kwargs: super(AsyncHTTPClient, cls).__new__(cls))

def test_http_client_init_with_default_async_client_class(mock_async_http_client):
    client = HTTPClient()
    assert not client._closed
    assert isinstance(client._async_client, AsyncHTTPClient)
    client._io_loop.close()

def test_http_client_init_with_custom_async_client_class(mock_async_http_client):
    class CustomAsyncHTTPClient(AsyncHTTPClient):
        pass

    client = HTTPClient(async_client_class=CustomAsyncHTTPClient)
    assert not client._closed
    assert isinstance(client._async_client, CustomAsyncHTTPClient)
    client._io_loop.close()

def test_http_client_init_with_kwargs(mock_async_http_client):
    client = HTTPClient(defaults={'user_agent': 'MyUserAgent'})
    assert not client._closed
    assert isinstance(client._async_client, AsyncHTTPClient)
    client._io_loop.close()
