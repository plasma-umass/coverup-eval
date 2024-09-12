# file: tornado/simple_httpclient.py:159-163
# asked: {"lines": [159, 160, 161, 162, 163], "branches": [[161, 162], [161, 163]]}
# gained: {"lines": [159, 160, 161, 162, 163], "branches": [[161, 162], [161, 163]]}

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.netutil import Resolver
from tornado.tcpclient import TCPClient
from unittest import mock

@pytest.fixture
def mock_resolver():
    return mock.Mock(spec=Resolver)

@pytest.fixture
def mock_tcp_client():
    return mock.Mock(spec=TCPClient)

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

def test_close_without_own_resolver(client, mock_tcp_client):
    client.own_resolver = False
    client.close()
    client.resolver.close.assert_not_called()
    mock_tcp_client.close.assert_called_once()
