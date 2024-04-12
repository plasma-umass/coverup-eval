# file tornado/httpclient.py:671-678
# lines [671, 672, 673, 674, 675, 676, 678]
# branches ['673->674', '673->675', '675->676', '675->678']

import pytest
from tornado.httpclient import HTTPResponse
from io import BytesIO
from unittest.mock import MagicMock

class DummyRequest:
    def __init__(self, url):
        self.url = url

@pytest.fixture
def mock_response(mocker):
    request = DummyRequest(url="http://example.com")
    response = HTTPResponse(request, 200)
    response.buffer = mocker.Mock(spec=BytesIO)
    response._body = None  # Ensure _body starts as None for each test
    return response

def test_httpresponse_body_with_none_buffer(mock_response):
    mock_response.buffer = None
    assert mock_response.body == b""

def test_httpresponse_body_with_empty_buffer(mock_response):
    mock_response.buffer.getvalue.return_value = b""
    assert mock_response.body == b""

def test_httpresponse_body_with_non_empty_buffer(mock_response):
    mock_response.buffer.getvalue.return_value = b"test"
    assert mock_response.body == b"test"
    # Call again to test caching behavior
    assert mock_response.body == b"test"
    mock_response.buffer.getvalue.assert_called_once()
