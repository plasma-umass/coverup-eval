# file: tornado/tcpclient.py:193-195
# asked: {"lines": [193, 194, 195], "branches": [[194, 0], [194, 195]]}
# gained: {"lines": [193, 194, 195], "branches": [[194, 0], [194, 195]]}

import pytest
from unittest.mock import MagicMock
from tornado.iostream import IOStream
from tornado.concurrent import Future
from tornado.ioloop import IOLoop
import socket

# Assuming _Connector is imported from the module where it is defined
from tornado.tcpclient import _Connector

@pytest.fixture
def connector():
    addrinfo = [(socket.AF_INET, ('127.0.0.1', 80))]
    connect = MagicMock(return_value=(MagicMock(spec=IOStream), Future()))
    return _Connector(addrinfo, connect)

def test_close_streams(connector):
    # Create mock streams and add them to the connector's streams set
    stream1 = MagicMock(spec=IOStream)
    stream2 = MagicMock(spec=IOStream)
    connector.streams.add(stream1)
    connector.streams.add(stream2)

    # Call the method under test
    connector.close_streams()

    # Assert that close was called on each stream
    stream1.close.assert_called_once()
    stream2.close.assert_called_once()

    # Clean up
    connector.streams.clear()
