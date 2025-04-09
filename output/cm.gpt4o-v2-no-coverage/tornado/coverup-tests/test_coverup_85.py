# file: tornado/tcpclient.py:205-211
# asked: {"lines": [205, 206, 207, 208, 210, 211], "branches": [[206, 207], [206, 210]]}
# gained: {"lines": [205, 206, 207, 208, 210, 211], "branches": [[206, 207], [206, 210]]}

import pytest
import socket
from tornado.tcpclient import TCPClient
from tornado.netutil import Resolver

class MockResolver(Resolver):
    def resolve(self, host, port, family=socket.AF_UNSPEC):
        return []

    def close(self):
        pass

def test_tcpclient_with_custom_resolver():
    mock_resolver = MockResolver()
    client = TCPClient(resolver=mock_resolver)
    assert client.resolver is mock_resolver
    assert not client._own_resolver

def test_tcpclient_with_default_resolver(mocker):
    mocker.patch('tornado.netutil.Resolver.configurable_default', return_value=MockResolver)
    client = TCPClient()
    assert isinstance(client.resolver, MockResolver)
    assert client._own_resolver
