# file: tornado/tcpclient.py:213-215
# asked: {"lines": [215], "branches": [[214, 215]]}
# gained: {"lines": [215], "branches": [[214, 215]]}

import pytest
from unittest.mock import Mock
from tornado.tcpclient import TCPClient
from tornado.netutil import Resolver

@pytest.fixture
def mock_resolver():
    return Mock(spec=Resolver)

def test_tcpclient_close_with_own_resolver(mock_resolver):
    client = TCPClient()
    client.resolver = mock_resolver
    client._own_resolver = True

    client.close()

    mock_resolver.close.assert_called_once()

def test_tcpclient_close_without_own_resolver(mock_resolver):
    client = TCPClient(resolver=mock_resolver)
    client._own_resolver = False

    client.close()

    mock_resolver.close.assert_not_called()
