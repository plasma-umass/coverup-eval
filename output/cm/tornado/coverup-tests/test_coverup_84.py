# file tornado/httpclient.py:115-120
# lines [115, 117, 118, 119, 120]
# branches ['117->exit', '117->118']

import pytest
from tornado.httpclient import HTTPClient
from unittest.mock import MagicMock

@pytest.fixture
def mock_http_client(mocker):
    client = HTTPClient()
    client._async_client = MagicMock()
    client._io_loop = MagicMock()
    client._closed = False
    return client

def test_http_client_close(mock_http_client):
    assert not mock_http_client._closed
    mock_http_client.close()
    mock_http_client._async_client.close.assert_called_once()
    mock_http_client._io_loop.close.assert_called_once()
    assert mock_http_client._closed

def test_http_client_close_already_closed(mock_http_client):
    mock_http_client._closed = True
    mock_http_client.close()
    mock_http_client._async_client.close.assert_not_called()
    mock_http_client._io_loop.close.assert_not_called()
