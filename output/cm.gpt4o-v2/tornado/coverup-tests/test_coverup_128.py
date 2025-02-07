# file: tornado/tcpclient.py:166-169
# asked: {"lines": [166, 167, 168, 169], "branches": [[168, 0], [168, 169]]}
# gained: {"lines": [166, 167, 168, 169], "branches": [[168, 169]]}

import pytest
import socket
from unittest import mock
from tornado.concurrent import Future
from tornado.ioloop import IOLoop
from tornado.iostream import IOStream
from tornado.tcpclient import _Connector

@pytest.fixture
def connector():
    addrinfo = [
        (socket.AF_INET, ('127.0.0.1', 80)),
        (socket.AF_INET6, ('::1', 80))
    ]
    connect = mock.Mock()
    return _Connector(addrinfo, connect)

def test_on_timeout(connector, monkeypatch):
    future_mock = mock.Mock(spec=Future)
    future_mock.done.return_value = False
    connector.future = future_mock

    try_connect_mock = mock.Mock()
    monkeypatch.setattr(connector, 'try_connect', try_connect_mock)

    connector.on_timeout()

    assert connector.timeout is None
    assert try_connect_mock.called
    assert list(try_connect_mock.call_args[0][0]) == list(iter(connector.secondary_addrs))
