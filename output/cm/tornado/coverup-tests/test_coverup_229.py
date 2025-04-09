# file tornado/simple_httpclient.py:89-157
# lines [148, 149, 154, 155]
# branches ['147->148', '153->154']

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.concurrent import Future
from tornado.ioloop import IOLoop
from tornado.httpclient import HTTPRequest
from unittest.mock import Mock
from tornado.netutil import OverrideResolver

@pytest.fixture
def mock_resolver():
    resolver = Mock()
    resolver.resolve = Mock(return_value=Future())
    resolver.resolve.return_value.set_result([])
    return resolver

@pytest.fixture
def mock_tcp_client(mocker):
    return mocker.patch('tornado.simple_httpclient.TCPClient')

@pytest.fixture
def mock_ioloop(mocker):
    return mocker.patch('tornado.ioloop.IOLoop.current')

def test_simple_async_http_client_with_custom_resolver(mock_resolver, mock_tcp_client, mock_ioloop):
    client = SimpleAsyncHTTPClient(resolver=mock_resolver)
    assert client.resolver == mock_resolver
    assert not client.own_resolver

def test_simple_async_http_client_with_hostname_mapping(mock_resolver, mock_tcp_client, mock_ioloop):
    hostname_mapping = {'example.com': '127.0.0.1'}
    client = SimpleAsyncHTTPClient(hostname_mapping=hostname_mapping, resolver=mock_resolver)
    assert isinstance(client.resolver, OverrideResolver)
    assert client.resolver.mapping == hostname_mapping
