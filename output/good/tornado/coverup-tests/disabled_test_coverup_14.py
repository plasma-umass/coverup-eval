# file tornado/simple_httpclient.py:89-157
# lines [89, 91, 92, 93, 94, 95, 96, 97, 131, 132, 133, 134, 136, 137, 139, 140, 142, 143, 144, 147, 148, 149, 151, 152, 153, 154, 155, 157]
# branches ['147->148', '147->151', '153->154', '153->157']

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.httpclient import HTTPRequest
from tornado.concurrent import Future
from tornado.ioloop import IOLoop
from unittest.mock import Mock

@pytest.fixture
def mock_resolver():
    resolver = Mock()
    resolver.resolve = Mock(return_value=Future())
    resolver.resolve.return_value.set_result([])
    return resolver

@pytest.fixture
def mock_tcp_client():
    tcp_client = Mock()
    return tcp_client

@pytest.fixture
def mock_ioloop():
    io_loop = Mock(spec=IOLoop)
    return io_loop

def test_simple_async_http_client_with_custom_resolver(mock_resolver, mock_tcp_client, mock_ioloop):
    hostname_mapping = {'example.com': '127.0.0.1'}
    client = SimpleAsyncHTTPClient(
        max_clients=10,
        hostname_mapping=hostname_mapping,
        resolver=mock_resolver,
        max_buffer_size=104857600,
        max_header_size=20480,
        max_body_size=10485760
    )
    assert client.resolver is not None
    assert client.max_clients == 10
    assert client.max_buffer_size == 104857600
    assert client.max_header_size == 20480
    assert client.max_body_size == 10485760
    assert client.own_resolver is False

    # Clean up
    client.close()

def test_simple_async_http_client_without_custom_resolver(mock_tcp_client, mock_ioloop):
    client = SimpleAsyncHTTPClient(
        max_clients=10,
        max_buffer_size=104857600,
        max_header_size=20480,
        max_body_size=10485760
    )
    assert client.resolver is not None
    assert client.max_clients == 10
    assert client.max_buffer_size == 104857600
    assert client.max_header_size == 20480
    assert client.max_body_size == 10485760
    assert client.own_resolver is True

    # Clean up
    client.close()
