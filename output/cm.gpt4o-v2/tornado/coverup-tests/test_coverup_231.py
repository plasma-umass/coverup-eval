# file: tornado/tcpclient.py:129-159
# asked: {"lines": [141, 149, 150, 155], "branches": [[140, 141], [146, 149], [153, 155]]}
# gained: {"lines": [149, 150, 155], "branches": [[146, 149], [153, 155]]}

import pytest
from unittest.mock import Mock, patch
from tornado.concurrent import Future
from tornado.iostream import IOStream
import socket

@pytest.fixture
def connector():
    from tornado.ioloop import IOLoop
    from tornado.tcpclient import _Connector

    addrinfo = [(socket.AF_INET, ('127.0.0.1', 80))]
    connect = Mock()
    connector = _Connector(addrinfo, connect)
    connector.io_loop = Mock(spec=IOLoop)
    return connector

def test_on_connect_done_future_done(connector):
    future = Future()
    future.set_result(IOStream(socket.socket()))
    connector.future.set_result(None)
    connector.on_connect_done(iter([]), socket.AF_INET, ('127.0.0.1', 80), future)
    assert connector.future.done()

def test_on_connect_done_with_exception(connector):
    future = Future()
    future.set_exception(Exception("Test exception"))
    connector.future = Future()
    connector.remaining = 1
    connector.last_error = None
    connector.timeout = None

    with patch.object(connector, 'try_connect') as mock_try_connect:
        connector.on_connect_done(iter([]), socket.AF_INET, ('127.0.0.1', 80), future)
        assert connector.last_error is not None
        mock_try_connect.assert_called_once()

def test_on_connect_done_with_timeout(connector):
    future = Future()
    future.set_exception(Exception("Test exception"))
    connector.future = Future()
    connector.remaining = 1
    connector.last_error = None
    connector.timeout = object()

    with patch.object(connector, 'try_connect') as mock_try_connect, \
         patch.object(connector.io_loop, 'remove_timeout') as mock_remove_timeout, \
         patch.object(connector, 'on_timeout') as mock_on_timeout:
        connector.on_connect_done(iter([]), socket.AF_INET, ('127.0.0.1', 80), future)
        assert connector.last_error is not None
        mock_try_connect.assert_called_once()
        mock_remove_timeout.assert_called_once_with(connector.timeout)
        mock_on_timeout.assert_called_once()

def test_on_connect_done_stream_close(connector):
    future = Future()
    stream = Mock(spec=IOStream)
    future.set_result(stream)
    connector.future.set_result(None)

    connector.on_connect_done(iter([]), socket.AF_INET, ('127.0.0.1', 80), future)
    stream.close.assert_called_once()
