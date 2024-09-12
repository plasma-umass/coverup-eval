# file: tornado/tcpclient.py:175-180
# asked: {"lines": [178, 179], "branches": []}
# gained: {"lines": [178, 179], "branches": []}

import pytest
from unittest.mock import Mock
import datetime
from tornado.ioloop import IOLoop
from tornado.tcpclient import _Connector

@pytest.fixture
def connector():
    addrinfo = [(Mock(), Mock())]
    connect = Mock()
    return _Connector(addrinfo, connect)

def test_set_connect_timeout(connector, monkeypatch):
    mock_ioloop = Mock(spec=IOLoop)
    monkeypatch.setattr(connector, 'io_loop', mock_ioloop)
    
    connect_timeout = 10.0
    connector.set_connect_timeout(connect_timeout)
    
    mock_ioloop.add_timeout.assert_called_once_with(connect_timeout, connector.on_connect_timeout)
    assert connector.connect_timeout is not None
