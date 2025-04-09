# file: tornado/httpclient.py:115-120
# asked: {"lines": [115, 117, 118, 119, 120], "branches": [[117, 0], [117, 118]]}
# gained: {"lines": [115, 117, 118, 119, 120], "branches": [[117, 0], [117, 118]]}

import pytest
from unittest import mock
from tornado.httpclient import HTTPClient

@pytest.fixture
def http_client():
    client = HTTPClient()
    client._closed = False
    client._async_client = mock.Mock()
    client._io_loop = mock.Mock()
    yield client
    client._async_client.close.assert_called_once()
    client._io_loop.close.assert_called_once()
    assert client._closed

def test_http_client_close(http_client):
    http_client.close()
