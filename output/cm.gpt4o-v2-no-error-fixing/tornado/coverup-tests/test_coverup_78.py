# file: tornado/httpclient.py:115-120
# asked: {"lines": [115, 117, 118, 119, 120], "branches": [[117, 0], [117, 118]]}
# gained: {"lines": [115, 117, 118, 119, 120], "branches": [[117, 0], [117, 118]]}

import pytest
from tornado.httpclient import HTTPClient
from tornado.ioloop import IOLoop
from unittest.mock import MagicMock

@pytest.fixture
def http_client():
    client = HTTPClient()
    yield client
    if not client._closed:
        client.close()

def test_http_client_close(http_client, mocker):
    # Ensure the client is not closed initially
    http_client._closed = False

    # Mock the async client and io loop close methods
    mock_async_client_close = mocker.patch.object(http_client._async_client, 'close')
    mock_io_loop_close = mocker.patch.object(http_client._io_loop, 'close')

    # Call the close method
    http_client.close()

    # Assert the close methods were called
    mock_async_client_close.assert_called_once()
    mock_io_loop_close.assert_called_once()

    # Assert the client is marked as closed
    assert http_client._closed

def test_http_client_close_already_closed(http_client, mocker):
    # Ensure the client is already closed
    http_client._closed = True

    # Mock the async client and io loop close methods
    mock_async_client_close = mocker.patch.object(http_client._async_client, 'close')
    mock_io_loop_close = mocker.patch.object(http_client._io_loop, 'close')

    # Call the close method
    http_client.close()

    # Assert the close methods were not called
    mock_async_client_close.assert_not_called()
    mock_io_loop_close.assert_not_called()

    # Assert the client is still marked as closed
    assert http_client._closed
