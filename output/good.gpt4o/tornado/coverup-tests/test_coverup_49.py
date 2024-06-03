# file tornado/tcpclient.py:55-73
# lines [55, 62, 63, 65, 66, 68, 69, 70, 71, 72, 73]
# branches []

import pytest
from unittest.mock import Mock, patch
from tornado.ioloop import IOLoop
from tornado.concurrent import Future
from tornado.iostream import IOStream
import socket

# Assuming the _Connector class is part of a module named tornado.tcpclient
from tornado.tcpclient import _Connector

@pytest.fixture
def mock_ioloop(mocker):
    mock_loop = mocker.patch('tornado.ioloop.IOLoop.current', return_value=Mock(spec=IOLoop))
    return mock_loop

def test_connector_initialization(mock_ioloop):
    addrinfo = [
        (socket.AF_INET, ('127.0.0.1', 80)),
        (socket.AF_INET6, ('::1', 80))
    ]
    connect = Mock(return_value=(Mock(spec=IOStream), Future()))

    connector = _Connector(addrinfo, connect)

    assert connector.io_loop == mock_ioloop.return_value
    assert connector.connect == connect
    assert isinstance(connector.future, Future)
    assert connector.timeout is None
    assert connector.connect_timeout is None
    assert connector.last_error is None
    assert connector.remaining == len(addrinfo)
    assert len(connector.primary_addrs) + len(connector.secondary_addrs) == len(addrinfo)
    assert isinstance(connector.streams, set)

@pytest.fixture(autouse=True)
def cleanup():
    yield
    IOLoop.clear_instance()

