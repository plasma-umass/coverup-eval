# file tornado/tcpclient.py:193-195
# lines [193, 194, 195]
# branches ['194->exit', '194->195']

import pytest
from unittest import mock
from tornado.iostream import IOStream
from tornado.concurrent import Future
from tornado.ioloop import IOLoop

# Assuming the _Connector class is part of a module named tornado.tcpclient
from tornado.tcpclient import _Connector

def test_connector_close_streams():
    # Create a mock stream with a close method
    mock_stream1 = mock.Mock()
    mock_stream2 = mock.Mock()
    
    # Mock the required arguments for _Connector
    addrinfo = [("mock_address", 1234)]
    
    def mock_connect(family, address):
        return mock.Mock(spec=IOStream), Future()
    
    # Instantiate the _Connector class and assign mock streams to it
    connector = _Connector(addrinfo, mock_connect)
    connector.streams = [mock_stream1, mock_stream2]
    
    # Call the close_streams method
    connector.close_streams()
    
    # Assert that the close method was called on each stream
    mock_stream1.close.assert_called_once()
    mock_stream2.close.assert_called_once()
