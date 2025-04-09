# file: tornado/simple_httpclient.py:89-157
# asked: {"lines": [89, 91, 92, 93, 94, 95, 96, 97, 131, 132, 133, 134, 136, 137, 139, 140, 142, 143, 144, 147, 148, 149, 151, 152, 153, 154, 155, 157], "branches": [[147, 148], [147, 151], [153, 154], [153, 157]]}
# gained: {"lines": [89, 91, 92, 93, 94, 95, 96, 97, 131, 132, 133, 134, 136, 137, 139, 140, 142, 143, 144, 147, 148, 149, 151, 152, 153, 154, 155, 157], "branches": [[147, 148], [147, 151], [153, 154], [153, 157]]}

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.httpclient import AsyncHTTPClient
from tornado.netutil import Resolver, OverrideResolver
from tornado.tcpclient import TCPClient
from unittest.mock import Mock, patch

@pytest.fixture
def mock_resolver():
    return Mock(spec=Resolver)

@pytest.fixture
def mock_tcp_client():
    return Mock(spec=TCPClient)

def test_initialize_defaults():
    client = SimpleAsyncHTTPClient()
    client.initialize()
    assert client.max_clients == 10
    assert client.max_buffer_size == 104857600
    assert client.max_header_size is None
    assert client.max_body_size is None
    assert isinstance(client.resolver, Resolver)
    assert client.own_resolver is True
    assert isinstance(client.tcp_client, TCPClient)

def test_initialize_with_params(mock_resolver, mock_tcp_client):
    hostname_mapping = {'example.com': '127.0.0.1'}
    with patch('tornado.simple_httpclient.Resolver', return_value=mock_resolver), \
         patch('tornado.simple_httpclient.TCPClient', return_value=mock_tcp_client):
        client = SimpleAsyncHTTPClient()
        client.initialize(
            max_clients=5,
            hostname_mapping=hostname_mapping,
            max_buffer_size=2048,
            resolver=mock_resolver,
            max_header_size=512,
            max_body_size=1024
        )
        assert client.max_clients == 5
        assert client.max_buffer_size == 2048
        assert client.max_header_size == 512
        assert client.max_body_size == 1024
        assert isinstance(client.resolver, OverrideResolver)
        assert client.resolver.resolver == mock_resolver
        assert client.own_resolver is False
        assert isinstance(client.tcp_client, TCPClient)
        assert client.resolver.mapping == hostname_mapping

def test_initialize_without_hostname_mapping(mock_resolver, mock_tcp_client):
    with patch('tornado.simple_httpclient.Resolver', return_value=mock_resolver), \
         patch('tornado.simple_httpclient.TCPClient', return_value=mock_tcp_client):
        client = SimpleAsyncHTTPClient()
        client.initialize(
            max_clients=5,
            max_buffer_size=2048,
            resolver=mock_resolver,
            max_header_size=512,
            max_body_size=1024
        )
        assert client.max_clients == 5
        assert client.max_buffer_size == 2048
        assert client.max_header_size == 512
        assert client.max_body_size == 1024
        assert client.resolver == mock_resolver
        assert client.own_resolver is False
        assert isinstance(client.tcp_client, TCPClient)
        assert not isinstance(client.resolver, OverrideResolver)
