# file tornado/simple_httpclient.py:687-694
# lines [690, 692]
# branches ['688->690', '691->692']

import pytest
from tornado import simple_httpclient, httputil
from unittest.mock import Mock, create_autospec

@pytest.fixture
def mock_http_connection():
    request = simple_httpclient.HTTPRequest(url='http://example.com', streaming_callback=Mock())
    release_callback = Mock()
    final_callback = Mock()
    max_buffer_size = 1048576
    tcp_client = create_autospec(simple_httpclient.SimpleAsyncHTTPClient)
    max_header_size = 65536
    max_body_size = 1048576
    connection = simple_httpclient._HTTPConnection(
        httputil.HTTPHeaders(), request, release_callback, final_callback,
        max_buffer_size, tcp_client, max_header_size, max_body_size
    )
    connection._should_follow_redirect = Mock(return_value=False)
    return connection, request.streaming_callback

def test_data_received_with_streaming_callback(mock_http_connection):
    connection, streaming_callback = mock_http_connection
    chunk = b'test_chunk'
    
    connection.data_received(chunk)
    
    streaming_callback.assert_called_once_with(chunk)
    assert not connection.chunks  # Ensure chunks list is still empty

def test_data_received_with_redirect(mock_http_connection):
    connection, _ = mock_http_connection
    connection._should_follow_redirect.return_value = True
    chunk = b'test_chunk'
    
    connection.data_received(chunk)
    
    # No assertions needed as we're testing that nothing happens when redirect is followed
    assert connection._should_follow_redirect.called
    assert not connection.chunks  # Ensure chunks list is still empty

# Cleanup is handled by the fixture, no top-level code needed.
