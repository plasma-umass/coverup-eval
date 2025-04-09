# file: tornado/tcpclient.py:213-215
# asked: {"lines": [213, 214, 215], "branches": [[214, 0], [214, 215]]}
# gained: {"lines": [213, 214, 215], "branches": [[214, 0], [214, 215]]}

import pytest
from unittest import mock
from tornado.tcpclient import TCPClient

@pytest.fixture
def tcp_client():
    client = TCPClient()
    client._own_resolver = True
    client.resolver = mock.Mock()
    return client

def test_tcp_client_close_with_own_resolver(tcp_client):
    tcp_client.close()
    tcp_client.resolver.close.assert_called_once()

def test_tcp_client_close_without_own_resolver():
    client = TCPClient()
    client._own_resolver = False
    client.resolver = mock.Mock()
    client.close()
    client.resolver.close.assert_not_called()
