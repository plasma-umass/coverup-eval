# file: tornado/tcpclient.py:166-169
# asked: {"lines": [167, 168, 169], "branches": [[168, 0], [168, 169]]}
# gained: {"lines": [167, 168, 169], "branches": [[168, 0], [168, 169]]}

import pytest
import socket
from unittest.mock import MagicMock, patch
from tornado.concurrent import Future
from tornado.ioloop import IOLoop
from tornado.tcpclient import _Connector

@pytest.fixture
def connector():
    addrinfo = [(socket.AF_INET, ('127.0.0.1', 80))]
    connect = MagicMock()
    return _Connector(addrinfo, connect)

def test_on_timeout_not_done(connector, monkeypatch):
    future = Future()
    connector.future = future
    connector.secondary_addrs = [(socket.AF_INET, ('127.0.0.1', 80))]
    try_connect_mock = MagicMock()
    monkeypatch.setattr(connector, 'try_connect', try_connect_mock)

    connector.on_timeout()

    assert connector.timeout is None
    assert try_connect_mock.called

def test_on_timeout_done(connector, monkeypatch):
    future = Future()
    future.set_result(None)
    connector.future = future
    try_connect_mock = MagicMock()
    monkeypatch.setattr(connector, 'try_connect', try_connect_mock)

    connector.on_timeout()

    assert connector.timeout is None
    assert not try_connect_mock.called
