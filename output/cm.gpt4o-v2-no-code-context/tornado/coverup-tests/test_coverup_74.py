# file: tornado/simple_httpclient.py:159-163
# asked: {"lines": [159, 160, 161, 162, 163], "branches": [[161, 162], [161, 163]]}
# gained: {"lines": [159, 160, 161, 162, 163], "branches": [[161, 162]]}

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop
from unittest.mock import MagicMock

@pytest.fixture
def mock_resolver(monkeypatch):
    mock_resolver = MagicMock()
    monkeypatch.setattr('tornado.simple_httpclient.Resolver', lambda *args, **kwargs: mock_resolver)
    return mock_resolver

@pytest.fixture
def mock_tcp_client(monkeypatch):
    mock_tcp_client = MagicMock()
    monkeypatch.setattr('tornado.simple_httpclient.TCPClient', lambda *args, **kwargs: mock_tcp_client)
    return mock_tcp_client

@pytest.fixture
def client(mock_resolver, mock_tcp_client):
    client = SimpleAsyncHTTPClient(IOLoop.current())
    client.own_resolver = True
    client.resolver = mock_resolver
    client.tcp_client = mock_tcp_client
    return client

def test_close(client, mock_resolver, mock_tcp_client):
    client.close()
    mock_resolver.close.assert_called_once()
    mock_tcp_client.close.assert_called_once()
