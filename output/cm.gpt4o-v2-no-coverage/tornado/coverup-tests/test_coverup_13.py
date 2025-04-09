# file: tornado/simple_httpclient.py:89-157
# asked: {"lines": [89, 91, 92, 93, 94, 95, 96, 97, 131, 132, 133, 134, 136, 137, 139, 140, 142, 143, 144, 147, 148, 149, 151, 152, 153, 154, 155, 157], "branches": [[147, 148], [147, 151], [153, 154], [153, 157]]}
# gained: {"lines": [89, 91, 92, 93, 94, 95, 96, 97, 131, 132, 133, 134, 136, 137, 139, 140, 142, 143, 144, 147, 148, 149, 151, 152, 153, 154, 155, 157], "branches": [[147, 148], [147, 151], [153, 154], [153, 157]]}

import pytest
from unittest.mock import MagicMock, patch
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.netutil import Resolver, OverrideResolver
from tornado.tcpclient import TCPClient
import collections

@pytest.fixture
def mock_resolver():
    return MagicMock(spec=Resolver)

@pytest.fixture
def mock_tcp_client():
    return MagicMock(spec=TCPClient)

def test_initialize_with_defaults(mock_resolver, mock_tcp_client):
    with patch('tornado.simple_httpclient.Resolver', return_value=mock_resolver), \
         patch('tornado.simple_httpclient.TCPClient', return_value=mock_tcp_client):
        client = SimpleAsyncHTTPClient()
        client.initialize()

        assert client.max_clients == 10
        assert isinstance(client.queue, collections.deque)
        assert client.active == {}
        assert client.waiting == {}
        assert client.max_buffer_size == 104857600
        assert client.max_header_size is None
        assert client.max_body_size is None
        assert client.resolver == mock_resolver
        assert client.own_resolver is True
        assert client.tcp_client == mock_tcp_client

def test_initialize_with_custom_resolver(mock_resolver, mock_tcp_client):
    with patch('tornado.simple_httpclient.TCPClient', return_value=mock_tcp_client):
        client = SimpleAsyncHTTPClient()
        client.initialize(resolver=mock_resolver)

        assert client.resolver == mock_resolver
        assert client.own_resolver is False
        assert client.tcp_client == mock_tcp_client

def test_initialize_with_hostname_mapping(mock_resolver, mock_tcp_client):
    hostname_mapping = {'example.com': '127.0.0.1'}
    with patch('tornado.simple_httpclient.Resolver', return_value=mock_resolver), \
         patch('tornado.simple_httpclient.OverrideResolver') as mock_override_resolver, \
         patch('tornado.simple_httpclient.TCPClient', return_value=mock_tcp_client):
        client = SimpleAsyncHTTPClient()
        client.initialize(hostname_mapping=hostname_mapping)

        mock_override_resolver.assert_called_once_with(resolver=mock_resolver, mapping=hostname_mapping)
        assert client.resolver == mock_override_resolver.return_value
        assert client.own_resolver is True
        assert client.tcp_client == mock_tcp_client
