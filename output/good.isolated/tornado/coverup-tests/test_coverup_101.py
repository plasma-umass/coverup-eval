# file tornado/tcpclient.py:213-215
# lines [213, 214, 215]
# branches ['214->exit', '214->215']

import pytest
from tornado.tcpclient import TCPClient
from unittest.mock import MagicMock

@pytest.fixture
def mock_resolver():
    resolver = MagicMock()
    resolver.close = MagicMock()
    return resolver

@pytest.fixture
def tcp_client(mock_resolver):
    client = TCPClient()
    client._own_resolver = True
    client.resolver = mock_resolver
    return client

def test_tcp_client_close(tcp_client, mock_resolver):
    tcp_client.close()
    mock_resolver.close.assert_called_once()

    # Cleanup
    tcp_client._own_resolver = False
    tcp_client.resolver = None
