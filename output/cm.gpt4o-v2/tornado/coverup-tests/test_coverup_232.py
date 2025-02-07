# file: tornado/tcpclient.py:187-191
# asked: {"lines": [189, 191], "branches": [[188, 189], [190, 191]]}
# gained: {"lines": [189, 191], "branches": [[188, 189], [190, 191]]}

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

def test_clear_timeouts(connector):
    mock_io_loop = mock.Mock(spec=IOLoop)
    connector.io_loop = mock_io_loop

    # Set timeouts to non-None values
    connector.timeout = object()
    connector.connect_timeout = object()

    connector.clear_timeouts()

    # Assert that remove_timeout was called for both timeouts
    mock_io_loop.remove_timeout.assert_any_call(connector.timeout)
    mock_io_loop.remove_timeout.assert_any_call(connector.connect_timeout)

    # Clean up
    connector.timeout = None
    connector.connect_timeout = None

def test_clear_timeouts_no_timeout(connector):
    mock_io_loop = mock.Mock(spec=IOLoop)
    connector.io_loop = mock_io_loop

    # Set timeouts to None
    connector.timeout = None
    connector.connect_timeout = None

    connector.clear_timeouts()

    # Assert that remove_timeout was not called
    mock_io_loop.remove_timeout.assert_not_called()
