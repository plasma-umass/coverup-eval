# file tornado/tcpclient.py:111-127
# lines [111, 112, 113, 114, 118, 119, 120, 122, 123, 124, 125, 126]
# branches ['118->119', '118->122']

import pytest
from unittest.mock import Mock, patch
from tornado.tcpclient import _Connector
from tornado.concurrent import Future
from tornado.iostream import IOStream
import socket

@pytest.fixture
def mock_connector():
    addrinfo = [(socket.AF_INET, (socket.SOCK_STREAM, None, None, None, ('127.0.0.1', 80)))]
    connector = _Connector(addrinfo, Mock())
    connector.remaining = 0
    connector.future = Future()
    connector.last_error = None
    connector.streams = set()
    connector.connect = Mock()
    return connector

def test_connector_try_connect_stop_iteration(mock_connector):
    mock_connector.connect.return_value = (IOStream(socket.socket()), Future())

    # Create an iterator that raises StopIteration
    addrs = iter([])

    with patch('tornado.tcpclient.future_add_done_callback') as mock_future_add_done_callback:
        mock_connector.try_connect(addrs)

    # Assert that the future was set with an exception
    assert mock_connector.future.done()
    with pytest.raises(IOError) as exc_info:
        mock_connector.future.result()
    assert str(exc_info.value) == "connection failed"

    # Assert that future_add_done_callback was not called
    mock_future_add_done_callback.assert_not_called()

    # Clean up
    for stream in mock_connector.streams:
        stream.close()
