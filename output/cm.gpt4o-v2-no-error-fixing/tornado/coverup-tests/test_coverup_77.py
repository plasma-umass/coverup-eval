# file: tornado/tcpclient.py:213-215
# asked: {"lines": [213, 214, 215], "branches": [[214, 0], [214, 215]]}
# gained: {"lines": [213, 214, 215], "branches": [[214, 0], [214, 215]]}

import pytest
from unittest import mock
from tornado.tcpclient import TCPClient
from tornado.netutil import Resolver

@pytest.fixture
def tcp_client():
    return TCPClient()

def test_tcp_client_close_with_own_resolver():
    resolver_mock = mock.Mock(spec=Resolver)
    client = TCPClient(resolver=resolver_mock)
    client._own_resolver = True  # Ensure _own_resolver is True
    client.close()
    resolver_mock.close.assert_called_once()

def test_tcp_client_close_without_own_resolver():
    resolver_mock = mock.Mock(spec=Resolver)
    client = TCPClient(resolver=resolver_mock)
    client._own_resolver = False  # Ensure _own_resolver is False
    client.close()
    resolver_mock.close.assert_not_called()
