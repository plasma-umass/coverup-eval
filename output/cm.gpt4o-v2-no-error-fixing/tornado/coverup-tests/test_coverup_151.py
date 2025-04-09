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

def test_initialize_with_resolver(mock_resolver):
    client = SimpleAsyncHTTPClient(resolver=mock_resolver)
    assert client.resolver == mock_resolver
    assert client.own_resolver is False

def test_initialize_with_hostname_mapping(mock_resolver, mock_override_resolver, monkeypatch):
    def mock_override_resolver_init(self, resolver, mapping):
        self.resolver = resolver
        self.mapping = mapping

    monkeypatch.setattr(OverrideResolver, 'initialize', mock_override_resolver_init)
    hostname_mapping = {"example.com": "127.0.0.1"}
    client = SimpleAsyncHTTPClient(resolver=mock_resolver, hostname_mapping=hostname_mapping)
    assert isinstance(client.resolver, OverrideResolver)
    assert client.resolver.mapping == hostname_mapping

def test_initialize_without_resolver():
    client = SimpleAsyncHTTPClient()
    assert isinstance(client.resolver, Resolver)
    assert client.own_resolver is True

def test_initialize_without_hostname_mapping():
    client = SimpleAsyncHTTPClient()
    assert not isinstance(client.resolver, OverrideResolver)
