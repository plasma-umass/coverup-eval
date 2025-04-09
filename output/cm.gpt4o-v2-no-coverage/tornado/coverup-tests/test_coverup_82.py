# file: tornado/tcpclient.py:182-185
# asked: {"lines": [182, 183, 184, 185], "branches": [[183, 184], [183, 185]]}
# gained: {"lines": [182, 183, 184, 185], "branches": [[183, 184], [183, 185]]}

import pytest
from unittest.mock import Mock, patch
from tornado.gen import TimeoutError
from tornado.concurrent import Future
from tornado.tcpclient import _Connector

@pytest.fixture
def connector():
    addrinfo = [(Mock(), Mock())]
    connect = Mock()
    return _Connector(addrinfo, connect)

def test_on_connect_timeout(connector):
    future = Future()
    connector.future = future
    connector.close_streams = Mock()

    with patch.object(connector, 'close_streams') as mock_close_streams:
        connector.on_connect_timeout()
        assert future.done()
        assert isinstance(future.exception(), TimeoutError)
        mock_close_streams.assert_called_once()

def test_on_connect_timeout_future_done(connector):
    future = Future()
    future.set_result(None)
    connector.future = future
    connector.close_streams = Mock()

    with patch.object(connector, 'close_streams') as mock_close_streams:
        connector.on_connect_timeout()
        assert future.done()
        assert future.exception() is None
        mock_close_streams.assert_called_once()
