# file: tornado/tcpclient.py:193-195
# asked: {"lines": [193, 194, 195], "branches": [[194, 0], [194, 195]]}
# gained: {"lines": [193, 194, 195], "branches": [[194, 0], [194, 195]]}

import pytest
from unittest.mock import Mock, create_autospec
from tornado.iostream import IOStream
from tornado.concurrent import Future
from tornado.ioloop import IOLoop
import socket

from tornado.tcpclient import _Connector

@pytest.fixture
def connector():
    addrinfo = [(socket.AF_INET, ('127.0.0.1', 80))]
    connect = Mock()
    connect.return_value = (create_autospec(IOStream), Future())
    return _Connector(addrinfo, connect)

def test_close_streams(connector):
    stream1 = create_autospec(IOStream)
    stream2 = create_autospec(IOStream)
    connector.streams = {stream1, stream2}
    
    connector.close_streams()
    
    stream1.close.assert_called_once()
    stream2.close.assert_called_once()
    assert all(stream.close.called for stream in connector.streams)

def test_on_connect_done_with_exception(connector):
    addrs = iter([(socket.AF_INET, ('127.0.0.1', 80))])
    af = socket.AF_INET
    addr = ('127.0.0.1', 80)
    future = Future()
    future.set_exception(IOError("connection failed"))
    
    connector.on_connect_done(addrs, af, addr, future)
    
    assert connector.remaining == 0
    assert isinstance(connector.last_error, IOError)
    assert not connector.future.done()

def test_on_connect_done_success(connector):
    addrs = iter([(socket.AF_INET, ('127.0.0.1', 80))])
    af = socket.AF_INET
    addr = ('127.0.0.1', 80)
    future = Future()
    stream = create_autospec(IOStream)
    future.set_result(stream)
    
    connector.on_connect_done(addrs, af, addr, future)
    
    assert connector.future.done()
    assert connector.future.result() == (af, addr, stream)
    assert not stream.close.called
