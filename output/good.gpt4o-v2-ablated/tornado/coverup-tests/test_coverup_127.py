# file: tornado/simple_httpclient.py:159-163
# asked: {"lines": [], "branches": [[161, 163]]}
# gained: {"lines": [], "branches": [[161, 163]]}

import pytest
from tornado.httpclient import AsyncHTTPClient
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from unittest.mock import MagicMock

@pytest.fixture
def mock_resolver():
    resolver = MagicMock()
    return resolver

@pytest.fixture
def mock_tcp_client():
    tcp_client = MagicMock()
    return tcp_client

@pytest.fixture
def client(mock_resolver, mock_tcp_client):
    client = SimpleAsyncHTTPClient()
    client.own_resolver = True
    client.resolver = mock_resolver
    client.tcp_client = mock_tcp_client
    return client

def test_close_with_own_resolver(client, mock_resolver, mock_tcp_client):
    client.close()
    mock_resolver.close.assert_called_once()
    mock_tcp_client.close.assert_called_once()

def test_close_without_own_resolver(client, mock_resolver, mock_tcp_client):
    client.own_resolver = False
    client.close()
    mock_resolver.close.assert_not_called()
    mock_tcp_client.close.assert_called_once()
