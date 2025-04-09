# file: tornado/tcpclient.py:171-173
# asked: {"lines": [172, 173], "branches": [[172, 0], [172, 173]]}
# gained: {"lines": [172, 173], "branches": [[172, 0], [172, 173]]}

import pytest
from tornado.ioloop import IOLoop
from tornado.concurrent import Future
from tornado.iostream import IOStream
from unittest.mock import Mock, call
import socket

from tornado.tcpclient import _Connector

@pytest.fixture
def connector():
    addrinfo = [(socket.AF_INET, ('127.0.0.1', 80))]
    connect = Mock(return_value=(Mock(spec=IOStream), Future()))
    return _Connector(addrinfo, connect)

def test_clear_timeout(connector, mocker):
    mock_io_loop = mocker.patch.object(connector, 'io_loop')
    connector.timeout = mocker.Mock()
    connector.clear_timeout()
    mock_io_loop.remove_timeout.assert_called_once_with(connector.timeout)

def test_clear_timeout_no_timeout(connector, mocker):
    mock_io_loop = mocker.patch.object(connector, 'io_loop')
    connector.timeout = None
    connector.clear_timeout()
    mock_io_loop.remove_timeout.assert_not_called()
