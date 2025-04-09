# file: tornado/simple_httpclient.py:159-163
# asked: {"lines": [], "branches": [[161, 163]]}
# gained: {"lines": [], "branches": [[161, 163]]}

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.httpclient import AsyncHTTPClient
from unittest.mock import Mock, patch

@pytest.fixture
def mock_resolver():
    return Mock()

@pytest.fixture
def mock_tcp_client():
    return Mock()

@pytest.fixture
def client(mock_resolver, mock_tcp_client):
    client = SimpleAsyncHTTPClient()
    client.resolver = mock_resolver
    client.tcp_client = mock_tcp_client
    client.own_resolver = True
    yield client
    client.close()

def test_close_with_own_resolver(client, mock_resolver, mock_tcp_client):
    client.close()
    mock_resolver.close.assert_called_once()
    mock_tcp_client.close.assert_called_once()

def test_close_without_own_resolver(client, mock_resolver, mock_tcp_client):
    client.own_resolver = False
    client.close()
    mock_resolver.close.assert_not_called()
    mock_tcp_client.close.assert_called_once()
