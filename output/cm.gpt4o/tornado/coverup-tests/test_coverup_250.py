# file tornado/tcpclient.py:213-215
# lines [215]
# branches ['214->215']

import pytest
from unittest import mock
from tornado.tcpclient import TCPClient

@pytest.fixture
def tcp_client():
    client = TCPClient()
    client._own_resolver = True
    client.resolver = mock.Mock()
    yield client
    client.close()

def test_tcp_client_close(tcp_client):
    tcp_client.close()
    tcp_client.resolver.close.assert_called_once()
