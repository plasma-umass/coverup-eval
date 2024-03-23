# file tornado/tcpclient.py:193-195
# lines [193, 194, 195]
# branches ['194->exit', '194->195']

import pytest
from tornado.tcpclient import _Connector
from unittest.mock import MagicMock

@pytest.fixture
def mock_stream():
    stream = MagicMock()
    return stream

@pytest.fixture
def connector_with_streams(mock_stream):
    addrinfo = MagicMock()
    connect = MagicMock()
    connector = _Connector(addrinfo, connect)
    connector.streams = [mock_stream]
    return connector

def test_connector_close_streams(connector_with_streams, mock_stream):
    # Precondition: Ensure streams are not already closed
    assert not mock_stream.close.called

    # Execute the method under test
    connector_with_streams.close_streams()

    # Postcondition: Ensure the stream is closed
    mock_stream.close.assert_called_once()

    # Cleanup is handled by the fixture's teardown
