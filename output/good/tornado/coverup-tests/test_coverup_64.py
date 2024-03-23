# file tornado/tcpclient.py:55-73
# lines [55, 62, 63, 65, 66, 68, 69, 70, 71, 72, 73]
# branches []

import pytest
from tornado.tcpclient import _Connector
from tornado.iostream import IOStream
from tornado.ioloop import IOLoop
from tornado.concurrent import Future
from unittest.mock import Mock
import socket

@pytest.fixture
def mock_ioloop(mocker):
    mock_loop = mocker.Mock(spec=IOLoop)
    mocker.patch('tornado.ioloop.IOLoop.current', return_value=mock_loop)
    return mock_loop

@pytest.fixture
def mock_connect(mocker):
    mock_connect = mocker.Mock(return_value=(Mock(spec=IOStream), Future()))
    return mock_connect

@pytest.fixture
def addrinfo():
    return [
        (socket.AF_INET, ('127.0.0.1', 80)),
    ]

@pytest.fixture
def connector_instance(mock_ioloop, mock_connect, addrinfo):
    return _Connector(addrinfo, mock_connect)

def test_connector_init(connector_instance, addrinfo):
    assert connector_instance.remaining == len(addrinfo)
    assert connector_instance.primary_addrs == addrinfo
    assert connector_instance.secondary_addrs == []
    assert connector_instance.streams == set()
    assert not connector_instance.future.done()
    assert connector_instance.timeout is None
    assert connector_instance.connect_timeout is None
    assert connector_instance.last_error is None
