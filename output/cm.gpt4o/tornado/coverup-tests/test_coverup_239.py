# file tornado/httpclient.py:198-214
# lines [205]
# branches ['204->205']

import pytest
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient

@pytest.fixture
def mock_ioloop(mocker):
    mock_ioloop = mocker.Mock(spec=IOLoop)
    mocker.patch('tornado.ioloop.IOLoop.current', return_value=mock_ioloop)
    return mock_ioloop

@pytest.fixture
def mock_async_clients(mocker):
    mock_async_clients = mocker.patch('tornado.httpclient.AsyncHTTPClient._async_clients', return_value={})
    return mock_async_clients

def test_async_http_client_instance_cache_hit(mock_ioloop, mock_async_clients, mocker):
    # Create a mock instance to be returned from the cache
    mock_instance = mocker.Mock(spec=AsyncHTTPClient)
    mock_async_clients.return_value[mock_ioloop] = mock_instance

    # Call the __new__ method and check if it returns the cached instance
    instance = AsyncHTTPClient()
    assert instance is mock_instance

    # Clean up
    del mock_async_clients.return_value[mock_ioloop]

def test_async_http_client_instance_cache_miss(mock_ioloop, mock_async_clients):
    # Ensure the cache is empty
    mock_async_clients.return_value.clear()

    # Call the __new__ method and check if it creates a new instance
    instance = AsyncHTTPClient()
    assert instance is not None
    assert isinstance(instance, AsyncHTTPClient)

    # Check if the new instance is added to the cache
    assert mock_ioloop in mock_async_clients.return_value
    assert mock_async_clients.return_value[mock_ioloop] is instance

    # Clean up
    del mock_async_clients.return_value[mock_ioloop]
