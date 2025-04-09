# file: tornado/tcpclient.py:129-159
# asked: {"lines": [129, 136, 137, 138, 139, 140, 141, 144, 145, 146, 149, 150, 151, 152, 153, 155, 157, 158, 159], "branches": [[140, 141], [140, 144], [146, 149], [146, 151], [153, 155], [153, 157]]}
# gained: {"lines": [129, 136, 137, 138, 139, 140, 144, 145, 146, 149, 150, 151, 152, 153, 155, 157, 158, 159], "branches": [[140, 144], [146, 149], [146, 151], [153, 155], [153, 157]]}

import pytest
from unittest.mock import Mock, MagicMock
import socket
from tornado.concurrent import Future
from tornado.ioloop import IOLoop
from tornado.iostream import IOStream
from typing import Tuple, Iterator

from tornado.tcpclient import _Connector

@pytest.fixture
def connector():
    addrinfo = [(socket.AF_INET, ('127.0.0.1', 80))]
    connect = Mock()
    return _Connector(addrinfo, connect)

def test_on_connect_done_success(connector, monkeypatch):
    future = Future()
    stream = MagicMock(spec=IOStream)
    future.set_result(stream)
    addrs = iter([(socket.AF_INET, ('127.0.0.1', 80))])
    
    connector.future = Future()
    connector.timeout = None
    connector.remaining = 1
    connector.streams = set([stream])
    
    connector.on_connect_done(addrs, socket.AF_INET, ('127.0.0.1', 80), future)
    
    assert connector.remaining == 0
    assert connector.future.done()
    assert connector.future.result() == (socket.AF_INET, ('127.0.0.1', 80), stream)
    assert stream.close.call_count == 0

def test_on_connect_done_failure(connector, monkeypatch):
    future = Future()
    future.set_exception(Exception("Connection error"))
    addrs = iter([(socket.AF_INET, ('127.0.0.1', 80))])
    
    connector.future = Future()
    connector.timeout = None
    connector.remaining = 1
    connector.streams = set()
    connector.last_error = None
    
    mock_try_connect = Mock()
    monkeypatch.setattr(connector, 'try_connect', mock_try_connect)
    
    connector.on_connect_done(addrs, socket.AF_INET, ('127.0.0.1', 80), future)
    
    assert connector.remaining == 0
    assert not connector.future.done()
    assert connector.last_error is not None
    mock_try_connect.assert_called_once_with(addrs)

def test_on_connect_done_timeout(connector, monkeypatch):
    future = Future()
    future.set_exception(Exception("Connection error"))
    addrs = iter([(socket.AF_INET, ('127.0.0.1', 80))])
    
    connector.future = Future()
    connector.timeout = object()
    connector.remaining = 1
    connector.streams = set()
    connector.last_error = None
    
    mock_try_connect = Mock()
    mock_remove_timeout = Mock()
    mock_on_timeout = Mock()
    monkeypatch.setattr(connector, 'try_connect', mock_try_connect)
    monkeypatch.setattr(connector.io_loop, 'remove_timeout', mock_remove_timeout)
    monkeypatch.setattr(connector, 'on_timeout', mock_on_timeout)
    
    connector.on_connect_done(addrs, socket.AF_INET, ('127.0.0.1', 80), future)
    
    assert connector.remaining == 0
    assert not connector.future.done()
    assert connector.last_error is not None
    mock_try_connect.assert_called_once_with(addrs)
    mock_remove_timeout.assert_called_once_with(connector.timeout)
    mock_on_timeout.assert_called_once()

def test_on_connect_done_late_arrival(connector, monkeypatch):
    future = Future()
    stream = MagicMock(spec=IOStream)
    future.set_result(stream)
    addrs = iter([(socket.AF_INET, ('127.0.0.1', 80))])
    
    connector.future = Future()
    connector.future.set_result(None)
    connector.timeout = None
    connector.remaining = 1
    connector.streams = set([stream])
    
    connector.on_connect_done(addrs, socket.AF_INET, ('127.0.0.1', 80), future)
    
    assert connector.remaining == 0
    assert stream.close.call_count == 1
