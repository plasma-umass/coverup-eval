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
    mock_async_client_close = mocker.patch.object(http_client._async_client, 'close')
    mock_io_loop_close = mocker.patch.object(http_client._io_loop, 'close')

    http_client.close()

    assert http_client._closed
    mock_async_client_close.assert_called_once()
    mock_io_loop_close.assert_called_once()

def test_http_client_double_close(http_client, mocker):
    mock_async_client_close = mocker.patch.object(http_client._async_client, 'close')
    mock_io_loop_close = mocker.patch.object(http_client._io_loop, 'close')

    http_client.close()
    http_client.close()  # Call close again to test idempotency

    assert http_client._closed
    mock_async_client_close.assert_called_once()
    mock_io_loop_close.assert_called_once()
