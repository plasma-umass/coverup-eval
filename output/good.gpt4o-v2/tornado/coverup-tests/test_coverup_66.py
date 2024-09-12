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
    assert client._own_resolver is False

def test_tcpclient_with_default_resolver(mocker):
    mocker.patch('tornado.netutil.Resolver', autospec=True)
    client = TCPClient()
    assert isinstance(client.resolver, Resolver)
    assert client._own_resolver is True
