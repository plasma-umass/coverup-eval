# file: tornado/simple_httpclient.py:89-157
# asked: {"lines": [148, 149, 154, 155], "branches": [[147, 148], [153, 154]]}
# gained: {"lines": [148, 149, 154, 155], "branches": [[147, 148], [153, 154]]}

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.httpclient import HTTPRequest, HTTPResponse
from tornado.ioloop import IOLoop
from tornado.netutil import Resolver, OverrideResolver
from tornado.tcpclient import TCPClient
import collections

@pytest.fixture
def mock_resolver(mocker):
    return mocker.Mock(spec=Resolver)

@pytest.fixture
def mock_tcp_client(mocker):
    return mocker.Mock(spec=TCPClient)

@pytest.fixture
def mock_override_resolver(mocker):
    return mocker.Mock(spec=OverrideResolver)

@pytest.fixture
def mock_ioloop(mocker):
    return mocker.Mock(spec=IOLoop)

def test_initialize_defaults(mocker, mock_resolver, mock_tcp_client, mock_override_resolver, mock_ioloop):
    mocker.patch('tornado.simple_httpclient.Resolver', return_value=mock_resolver)
    mocker.patch('tornado.simple_httpclient.TCPClient', return_value=mock_tcp_client)
    mocker.patch('tornado.simple_httpclient.OverrideResolver', return_value=mock_override_resolver)
    mocker.patch('tornado.ioloop.IOLoop.current', return_value=mock_ioloop)

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

def test_initialize_with_params(mocker, mock_resolver, mock_tcp_client, mock_override_resolver, mock_ioloop):
    mocker.patch('tornado.simple_httpclient.Resolver', return_value=mock_resolver)
    mocker.patch('tornado.simple_httpclient.TCPClient', return_value=mock_tcp_client)
    mocker.patch('tornado.simple_httpclient.OverrideResolver', return_value=mock_override_resolver)
    mocker.patch('tornado.ioloop.IOLoop.current', return_value=mock_ioloop)

    hostname_mapping = {'example.com': '127.0.0.1'}
    client = SimpleAsyncHTTPClient()
    client.initialize(
        max_clients=5,
        hostname_mapping=hostname_mapping,
        max_buffer_size=2048,
        resolver=mock_resolver,
        defaults={'user_agent': 'test-agent'},
        max_header_size=512,
        max_body_size=1024
    )

    assert client.max_clients == 5
    assert isinstance(client.queue, collections.deque)
    assert client.active == {}
    assert client.waiting == {}
    assert client.max_buffer_size == 2048
    assert client.max_header_size == 512
    assert client.max_body_size == 1024
    assert client.resolver == mock_override_resolver
    assert client.own_resolver is False
    assert client.tcp_client == mock_tcp_client
