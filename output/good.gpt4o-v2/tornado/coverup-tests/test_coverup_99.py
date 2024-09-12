# file: tornado/httpclient.py:115-120
# asked: {"lines": [115, 117, 118, 119, 120], "branches": [[117, 0], [117, 118]]}
# gained: {"lines": [115, 117, 118, 119, 120], "branches": [[117, 0], [117, 118]]}

import pytest
from tornado.httpclient import HTTPClient
from tornado.ioloop import IOLoop
from unittest.mock import MagicMock

@pytest.fixture
def http_client():
    io_loop = IOLoop(make_current=False)
    async_client = MagicMock()
    client = HTTPClient()
    client._io_loop = io_loop
    client._async_client = async_client
    client._closed = False
    yield client
    if not client._closed:
        client.close()

def test_http_client_close(http_client):
    http_client.close()
    assert http_client._closed
    http_client._async_client.close.assert_called_once()
    assert http_client._io_loop.asyncio_loop.is_closed()
