# file: tornado/tcpclient.py:171-173
# asked: {"lines": [172, 173], "branches": [[172, 0], [172, 173]]}
# gained: {"lines": [172, 173], "branches": [[172, 0], [172, 173]]}

import pytest
from unittest import mock
from tornado.ioloop import IOLoop
from tornado.concurrent import Future

# Assuming _Connector is imported from the module where it is defined
from tornado.tcpclient import _Connector

@pytest.fixture
def connector():
    addrinfo = [(mock.Mock(), mock.Mock())]
    connect = mock.Mock()
    return _Connector(addrinfo, connect)

def test_clear_timeout(connector):
    timeout_mock = mock.Mock()
    connector.timeout = timeout_mock
    connector.io_loop = mock.Mock()
    
    connector.clear_timeout()
    
    connector.io_loop.remove_timeout.assert_called_once_with(timeout_mock)
    assert connector.timeout == timeout_mock  # Ensure the timeout is not modified

def test_clear_timeout_no_timeout(connector):
    connector.timeout = None
    connector.io_loop = mock.Mock()
    
    connector.clear_timeout()
    
    connector.io_loop.remove_timeout.assert_not_called()
