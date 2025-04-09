# file: tornado/tcpclient.py:205-211
# asked: {"lines": [205, 206, 207, 208, 210, 211], "branches": [[206, 207], [206, 210]]}
# gained: {"lines": [205, 206, 207, 208, 210, 211], "branches": [[206, 207], [206, 210]]}

import pytest
from tornado.tcpclient import TCPClient
from tornado.netutil import Resolver

def test_tcpclient_with_custom_resolver():
    custom_resolver = Resolver()
    client = TCPClient(resolver=custom_resolver)
    assert client.resolver is custom_resolver
    assert not client._own_resolver

def test_tcpclient_with_default_resolver(monkeypatch):
    class MockResolver:
        def __init__(self):
            pass

    monkeypatch.setattr('tornado.tcpclient.Resolver', MockResolver)
    client = TCPClient()
    assert isinstance(client.resolver, MockResolver)
    assert client._own_resolver
