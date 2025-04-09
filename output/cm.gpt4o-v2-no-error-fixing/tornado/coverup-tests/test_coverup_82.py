# file: tornado/tcpclient.py:182-185
# asked: {"lines": [182, 183, 184, 185], "branches": [[183, 184], [183, 185]]}
# gained: {"lines": [182, 183, 184, 185], "branches": [[183, 184]]}

import pytest
from tornado.gen import TimeoutError
from tornado.concurrent import Future
from tornado.iostream import IOStream
from tornado.ioloop import IOLoop
from unittest import mock

from tornado.tcpclient import _Connector

@pytest.fixture
def connector():
    addrinfo = [(mock.Mock(), mock.Mock())]
    connect = mock.Mock()
    return _Connector(addrinfo, connect)

def test_on_connect_timeout(connector, monkeypatch):
    future = Future()
    connector.future = future

    # Ensure future is not done
    assert not connector.future.done()

    # Mock close_streams to avoid side effects
    close_streams_mock = mock.Mock()
    monkeypatch.setattr(connector, 'close_streams', close_streams_mock)

    # Call the method
    connector.on_connect_timeout()

    # Assert future is set with TimeoutError
    assert connector.future.done()
    assert isinstance(connector.future.exception(), TimeoutError)

    # Assert close_streams was called
    close_streams_mock.assert_called_once()

def test_close_streams(connector):
    # Create mock streams and add to connector
    stream1 = mock.Mock(spec=IOStream)
    stream2 = mock.Mock(spec=IOStream)
    connector.streams = {stream1, stream2}

    # Call the method
    connector.close_streams()

    # Assert all streams were closed
    stream1.close.assert_called_once()
    stream2.close.assert_called_once()
