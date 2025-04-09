# file: tornado/tcpclient.py:182-185
# asked: {"lines": [], "branches": [[183, 185]]}
# gained: {"lines": [], "branches": [[183, 185]]}

import pytest
from tornado.gen import TimeoutError
from tornado.concurrent import Future
from tornado.ioloop import IOLoop
from unittest import mock

from tornado.tcpclient import _Connector

@pytest.fixture
def connector():
    addrinfo = [(mock.Mock(), mock.Mock())]
    connect = mock.Mock()
    return _Connector(addrinfo, connect)

def test_on_connect_timeout_future_not_done(connector):
    connector.future = Future()
    connector.close_streams = mock.Mock()

    connector.on_connect_timeout()

    assert connector.future.done()
    assert isinstance(connector.future.exception(), TimeoutError)
    connector.close_streams.assert_called_once()

def test_on_connect_timeout_future_done(connector):
    connector.future = Future()
    connector.future.set_result(None)
    connector.close_streams = mock.Mock()

    connector.on_connect_timeout()

    assert connector.future.done()
    assert connector.future.result() is None
    connector.close_streams.assert_called_once()
