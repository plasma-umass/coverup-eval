# file: tornado/tcpclient.py:55-73
# asked: {"lines": [55, 62, 63, 65, 66, 68, 69, 70, 71, 72, 73], "branches": []}
# gained: {"lines": [55, 62, 63, 65, 66, 68, 69, 70, 71, 72, 73], "branches": []}

import pytest
from unittest.mock import Mock, patch
import socket
from tornado.concurrent import Future
from tornado.ioloop import IOLoop
from tornado.iostream import IOStream
from typing import Tuple, List, Callable
from tornado.tcpclient import _Connector

@pytest.fixture
def addrinfo():
    return [
        (socket.AF_INET, ('127.0.0.1', 80)),
        (socket.AF_INET6, ('::1', 80)),
        (socket.AF_INET, ('192.168.1.1', 80)),
    ]

@pytest.fixture
def connect():
    def mock_connect(af, addr):
        stream = Mock(spec=IOStream)
        future = Future()
        future.set_result(stream)
        return stream, future
    return mock_connect

def test_connector_init(addrinfo, connect):
    connector = _Connector(addrinfo, connect)
    
    assert connector.io_loop is IOLoop.current()
    assert connector.connect == connect
    assert isinstance(connector.future, Future)
    assert connector.timeout is None
    assert connector.connect_timeout is None
    assert connector.last_error is None
    assert connector.remaining == len(addrinfo)
    assert len(connector.primary_addrs) > 0
    assert len(connector.secondary_addrs) > 0
    assert isinstance(connector.streams, set)

def test_split(addrinfo):
    primary, secondary = _Connector.split(addrinfo)
    
    assert len(primary) > 0
    assert len(secondary) > 0
    assert all(af == socket.AF_INET for af, addr in primary)
    assert all(af == socket.AF_INET6 for af, addr in secondary)
