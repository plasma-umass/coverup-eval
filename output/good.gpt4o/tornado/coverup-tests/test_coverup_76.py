# file tornado/simple_httpclient.py:687-694
# lines [687, 688, 690, 691, 692, 694]
# branches ['688->690', '688->691', '691->692', '691->694']

import pytest
from tornado import httputil
from tornado.simple_httpclient import SimpleAsyncHTTPClient

class MockRequest:
    def __init__(self, streaming_callback=None):
        self.streaming_callback = streaming_callback

class MockHTTPConnection(httputil.HTTPMessageDelegate):
    def __init__(self, request):
        self.request = request
        self.chunks = []

    def data_received(self, chunk: bytes) -> None:
        if self._should_follow_redirect():
            return
        if self.request.streaming_callback is not None:
            self.request.streaming_callback(chunk)
        else:
            self.chunks.append(chunk)

    def _should_follow_redirect(self):
        return False

@pytest.fixture
def mock_request():
    return MockRequest()

@pytest.fixture
def mock_http_connection(mock_request):
    return MockHTTPConnection(mock_request)

def test_data_received_with_streaming_callback(mock_http_connection, mocker):
    mock_callback = mocker.Mock()
    mock_http_connection.request.streaming_callback = mock_callback
    chunk = b"test data"
    
    mock_http_connection.data_received(chunk)
    
    mock_callback.assert_called_once_with(chunk)

def test_data_received_without_streaming_callback(mock_http_connection):
    chunk = b"test data"
    
    mock_http_connection.data_received(chunk)
    
    assert mock_http_connection.chunks == [chunk]

def test_data_received_with_redirect(mock_http_connection, mocker):
    mocker.patch.object(mock_http_connection, '_should_follow_redirect', return_value=True)
    chunk = b"test data"
    
    mock_http_connection.data_received(chunk)
    
    assert mock_http_connection.chunks == []
