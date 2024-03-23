# file tornado/simple_httpclient.py:159-163
# lines []
# branches ['161->163']

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
    client.own_resolver = False  # Reset to not own the resolver before closing
    client.close()

def test_close_method_calls_resolver_and_tcp_client_close(http_client, mock_resolver, mock_tcp_client):
    http_client.close()
    mock_resolver.close.assert_called_once()
    mock_tcp_client.close.assert_called_once()

def test_close_method_with_own_resolver_false(http_client, mock_resolver, mock_tcp_client):
    http_client.own_resolver = False  # Set own_resolver to False to cover the branch
    http_client.close()
    mock_resolver.close.assert_not_called()  # Resolver's close should not be called
    mock_tcp_client.close.assert_called_once()  # tcp_client's close should still be called
