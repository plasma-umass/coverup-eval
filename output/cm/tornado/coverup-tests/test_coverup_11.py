# file tornado/simple_httpclient.py:514-527
# lines [514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527]
# branches ['515->516', '515->517', '517->518', '517->521', '519->520', '519->521', '522->exit', '522->523', '526->exit', '526->527']

import pytest
from tornado import httputil
from tornado.httpclient import HTTPRequest
from tornado.iostream import StreamClosedError
from unittest.mock import Mock, patch
import sys

# Assuming the _HTTPConnection class is in a module named tornado.simple_httpclient
from tornado.simple_httpclient import _HTTPConnection

@pytest.mark.asyncio
async def test_write_body_with_body_producer_and_stream_closed_error(mocker):
    # Mock the necessary parts
    mock_connection = Mock()
    mock_request = HTTPRequest(url='http://example.com', body_producer=lambda write: write(b'body'))
    mock_delegate = Mock()
    mock_handle_exception = mocker.patch.object(_HTTPConnection, '_handle_exception', return_value=False)

    # Create an instance of the _HTTPConnection
    http_connection = _HTTPConnection(mock_connection, mock_request, mock_delegate)

    # Mock the connection's read_response to raise StreamClosedError
    mock_connection.read_response.side_effect = StreamClosedError

    # Run the test
    with pytest.raises(StreamClosedError):
        await http_connection._write_body(start_read=True)

    # Assert that the body producer was called
    mock_request.body_producer.assert_called_once()

    # Assert that the connection's write method was called with the correct argument
    mock_connection.write.assert_called_once_with(b'body')

    # Assert that the connection's finish method was called
    mock_connection.finish.assert_called_once()

    # Assert that the connection's read_response was called
    mock_connection.read_response.assert_called_once()

    # Assert that the exception handler was called with the correct arguments
    exc_type, exc_value, _ = sys.exc_info()
    mock_handle_exception.assert_called_once_with(exc_type, exc_value, mocker.ANY)
