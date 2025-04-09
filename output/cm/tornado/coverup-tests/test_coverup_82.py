# file tornado/simple_httpclient.py:159-163
# lines [159, 160, 161, 162, 163]
# branches ['161->162', '161->163']

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from unittest.mock import MagicMock

@pytest.fixture
def mock_resolver():
    resolver = MagicMock()
    resolver.close = MagicMock()
    return resolver

@pytest.fixture
def mock_tcp_client():
    tcp_client = MagicMock()
    tcp_client.close = MagicMock()
    return tcp_client

@pytest.fixture
def http_client(mock_resolver, mock_tcp_client):
    client = SimpleAsyncHTTPClient()
    client.own_resolver = True
    client.resolver = mock_resolver
    client.tcp_client = mock_tcp_client
    yield client
    client.close()

def test_simple_async_http_client_close(http_client, mock_resolver, mock_tcp_client):
    http_client.close()
    mock_resolver.close.assert_called_once()
    mock_tcp_client.close.assert_called_once()
