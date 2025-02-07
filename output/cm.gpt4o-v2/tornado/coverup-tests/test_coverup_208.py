# file: tornado/simple_httpclient.py:89-157
# asked: {"lines": [148, 149, 154, 155], "branches": [[147, 148], [153, 154]]}
# gained: {"lines": [148, 149, 154, 155], "branches": [[147, 148], [153, 154]]}

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.netutil import Resolver, OverrideResolver
from tornado.tcpclient import TCPClient
from unittest.mock import Mock

@pytest.fixture
def mock_resolver():
    return Mock(spec=Resolver)

@pytest.fixture
def mock_override_resolver():
    return Mock(spec=OverrideResolver)

@pytest.fixture
def mock_tcp_client():
    return Mock(spec=TCPClient)

def test_initialize_with_resolver(mock_resolver, mock_tcp_client, monkeypatch):
    monkeypatch.setattr('tornado.simple_httpclient.Resolver', mock_resolver)
    monkeypatch.setattr('tornado.simple_httpclient.TCPClient', mock_tcp_client)
    
    client = SimpleAsyncHTTPClient()
    client.initialize(resolver=mock_resolver)
    
    assert client.resolver == mock_resolver
    assert client.own_resolver is False
    mock_tcp_client.assert_called_with(resolver=mock_resolver)

def test_initialize_with_hostname_mapping(mock_resolver, mock_override_resolver, mock_tcp_client, monkeypatch):
    monkeypatch.setattr('tornado.simple_httpclient.Resolver', mock_resolver)
    monkeypatch.setattr('tornado.simple_httpclient.OverrideResolver', mock_override_resolver)
    monkeypatch.setattr('tornado.simple_httpclient.TCPClient', mock_tcp_client)
    
    hostname_mapping = {'example.com': '127.0.0.1'}
    client = SimpleAsyncHTTPClient()
    client.initialize(hostname_mapping=hostname_mapping)
    
    mock_override_resolver.assert_called_with(resolver=mock_resolver(), mapping=hostname_mapping)
    assert client.resolver == mock_override_resolver()
    mock_tcp_client.assert_called_with(resolver=mock_override_resolver())
