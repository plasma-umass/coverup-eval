# file tornado/tcpclient.py:100-109
# lines [108]
# branches ['107->108']

import pytest
from tornado.tcpclient import _Connector
from tornado.iostream import IOStream
from unittest.mock import Mock, patch
from tornado.concurrent import Future
import socket

@pytest.fixture
def mock_connector(mocker):
    addrinfo = (socket.AF_INET, (Mock(), Mock()))
    connect = Mock()
    with patch('tornado.tcpclient._Connector.__init__', return_value=None) as mock_init:
        connector = _Connector(addrinfo, connect)
        connector.primary_addrs = [Mock()]
        connector.try_connect = Mock()
        connector.set_timeout = Mock()
        connector.set_connect_timeout = Mock()
        connector.future = Future()
        return connector

def test_connector_with_connect_timeout(mock_connector):
    connect_timeout = 10
    mock_connector.start(connect_timeout=connect_timeout)
    mock_connector.set_connect_timeout.assert_called_once_with(connect_timeout)
